import numpy as np
# import logging
import pandas as pd
import os
from numba import jit, prange

# logging.basicConfig(format='%(asctime)s\t\t%(message)s', level=logging.DEBUG)


def read_environmental_data(path):
    try:
        ghi_curve = pd.read_csv(path, usecols=[3], skiprows=341882).values
        temp = pd.read_csv(path, usecols=[2], skiprows=341882).values
    except pd.errors.EmptyDataError:
        ghi_curve = pd.read_csv(path, usecols=[3], skiprows=3).values * 1000
        temp = pd.read_csv(path, usecols=[5], skiprows=3).values
    return ghi_curve, temp


#  ghi_curve, temp = read_environmental_data()

@jit(nopython=True)
def pv_diesel_capacities(pv_capacity, battery_size, diesel_capacity, hour_numbers, temp, ghi, load_curve, k_t,
                         inv_eff, n_dis, n_chg, energy_per_hh):
    fuel_result = 0
    soc = 0.5
    unmet_demand = 0
    excess_gen = 0
    annual_diesel_gen = 0
    annual_battery_use = 0

    for hour in hour_numbers:
        hour = int(hour)
        # Battery self-discharge (0.02% per hour)
        annual_battery_use += 0.0002 * soc
        soc *= 0.9998
        soc_prev = soc * 1.0

        # Calculation of PV gen and net load
        t_cell = temp[hour] + 0.0256 * ghi[hour]  # PV cell temperature
        pv_gen = pv_capacity * 0.9 *  ghi[hour] / 1000 * (1 - k_t * (float(t_cell) - 25))  # PV generation in the hour
        net_load = load_curve[hour] - pv_gen * inv_eff  # remaining load not met by PV panels

        # Dispatchable energy from battery available to meet load
        battery_dispatchable = soc * battery_size * n_dis * inv_eff
        # Energy required to fully charge battery
        battery_chargeable = (1 - soc) * battery_size / n_chg / inv_eff

        # Below is the dispatch strategy for the diesel generator as described in word document

        if 4 < hour <= 17:
            # During the morning and day, the batteries are dispatched primarily.
            # The diesel generator, if needed, is run at the lowest possible capacity

            # Minimum diesel capacity to cover the net load after batteries.
            # Diesel genrator limited by lowest possible capacity (40%) and rated capacity
            min_diesel = min(max(net_load - battery_dispatchable, 0.4 * diesel_capacity), diesel_capacity)

            if net_load > battery_dispatchable:
                diesel_gen = min_diesel
            else:
                diesel_gen = 0

        elif 17 > hour > 23:
            # During the evening, the diesel generator is dispatched primarily, at max_diesel.
            # Batteries are dispatched if diesel generation is insufficient.

            #  Maximum amount of diesel needed to supply load and charge battery
            # Diesel genrator limited by lowest possible capacity (40%) and rated capacity
            max_diesel = max(min(net_load + battery_chargeable, diesel_capacity), 0.4 * diesel_capacity)
            max_diesel = max(min(net_load + battery_chargeable, diesel_capacity), 0.4 * diesel_capacity)

            if net_load > 0:
                diesel_gen = max_diesel
            else:
                diesel_gen = 0
        else:
            # During night, batteries are dispatched primarily.
            # The diesel generator is used at max_diesel if load is larger than battery capacity

            #  Maximum amount of diesel needed to supply load and charge battery
            # Diesel genrator limited by lowest possible capacity (40%) and rated capacity
            max_diesel = max(min(net_load + battery_chargeable, diesel_capacity), 0.4 * diesel_capacity)

            if net_load > battery_dispatchable:
                diesel_gen = max_diesel
            else:
                diesel_gen = 0

        if diesel_gen > 0:
            fuel_result = fuel_result + diesel_capacity * 0.08145 + diesel_gen * 0.246
            annual_diesel_gen += diesel_gen

        # Reamining load after diesel generator
        net_load = net_load - diesel_gen

        if net_load > 0:
            if diesel_gen > 0:
                # If diesel generation is used, but is smaller than load, battery is discharged
                soc = soc - net_load / n_dis / inv_eff / battery_size
            elif diesel_gen == 0:
                # If net load is positive and no diesel is used, battery is discharged
                soc = soc - net_load / n_dis / battery_size
        elif net_load < 0:
            if diesel_gen > 0:
                # If diesel generation is used, and is larger than load, battery is charged
                soc = soc - net_load * n_chg * inv_eff / battery_size
            if diesel_gen == 0:
                # If net load is negative, and no diesel has been used, excess PV gen is used to charge battery
                soc = soc - net_load * n_chg / battery_size

        if net_load > 0:
            hourly_battery_use = min(net_load / n_dis / battery_size, soc_prev)
            annual_battery_use += hourly_battery_use

        if battery_size > 0:
            if soc < 0:
                # If State of charge is negative, that means there's demand that could not be met.
                unmet_demand = unmet_demand - soc / n_dis * battery_size
                soc = 0

            if soc > 1:
                # If State of Charge is larger than 1, that means there was excess PV/diesel generation
                excess_gen = excess_gen + (soc - 1) / n_chg * battery_size
                soc = 1
        else:
            if net_load > 0:
                unmet_demand = unmet_demand + net_load

            if net_load < 0:
                excess_gen = excess_gen - net_load

    condition = unmet_demand / energy_per_hh  # LPSP is calculated
    excess_gen = excess_gen / energy_per_hh
    diesel_share = annual_diesel_gen / energy_per_hh
    battery_life = np.round(2000 / annual_battery_use)  # Run_Param Assuming 2000 full-load cycles for Li-ion batteries
    battery_life = np.minimum(battery_life, 20)

    return diesel_share, battery_life, condition, fuel_result, excess_gen


@jit(nopython=True)
def calculate_hybrid_lcoe(diesel_price, end_year, start_year, energy_per_hh,
                          fuel_usage, pv_panel_size, pv_cost, charge_controller, pv_om, diesel_capacity, diesel_cost,
                          diesel_om, inverter_life, load_curve, inverter_cost, diesel_life, pv_life, battery_life,
                          battery_size, battery_cost, dod_max, discount_rate):
    # Necessary information for calculation of LCOE is defined
    project_life = end_year - start_year
    generation = np.ones(project_life) * energy_per_hh
    generation[0] = 0

    # Calculate LCOE

    sum_el_gen = 0
    investment = 0
    sum_costs = 0
    npc = 0
    total_battery_investment = 0
    total_fuel_cost = 0
    total_om_cost = 0
    initial_investment = 0

    for year in prange(project_life + 1):
        salvage = 0
        inverter_investment = 0
        diesel_investment = 0
        pv_investment = 0
        battery_investment = 0

        fuel_costs = fuel_usage * diesel_price
        om_costs = (pv_panel_size * (pv_cost + charge_controller) * pv_om + diesel_capacity * diesel_cost * diesel_om)

        total_fuel_cost += fuel_costs / (1 + discount_rate) ** year
        total_om_cost += om_costs / (1 + discount_rate) ** year

        if year % inverter_life == 0:
            inverter_investment = max(load_curve) * inverter_cost  # Battery inverter
        if year % diesel_life == 0:
            diesel_investment = diesel_capacity * diesel_cost
        if year % pv_life == 0:
            pv_investment = pv_panel_size * (pv_cost + charge_controller + inverter_cost)  # PV inverter
        if year % battery_life == 0:
            battery_investment = battery_size * battery_cost / dod_max

        if year == project_life:
            salvage = (1 - (project_life % battery_life) / battery_life) * battery_cost * battery_size / dod_max + \
                      (1 - (project_life % diesel_life) / diesel_life) * diesel_capacity * diesel_cost + \
                      (1 - (project_life % pv_life) / pv_life) * pv_panel_size * (pv_cost + charge_controller + inverter_cost) + \
                      (1 - (project_life % inverter_life) / inverter_life) * max(load_curve) * inverter_cost

            total_battery_investment -= (1 - (project_life % battery_life) / battery_life) * battery_cost * battery_size / dod_max

        investment += diesel_investment + pv_investment + battery_investment + inverter_investment - salvage

        # if year == 0:
        #     initial_investment = diesel_investment + pv_investment + battery_investment + inverter_investment
        initial_investment += (diesel_investment + pv_investment + battery_investment + inverter_investment) / (
                (1 + discount_rate) ** year)


        sum_costs += (fuel_costs + om_costs + battery_investment + diesel_investment + pv_investment + inverter_investment - salvage) / (
                (1 + discount_rate) ** year)

        npc += (fuel_costs + om_costs + battery_investment + diesel_investment + pv_investment + inverter_investment) / (
                (1 + discount_rate) ** year)

        if year > 0:
            sum_el_gen += energy_per_hh / ((1 + discount_rate) ** year)

    emission_factor = fuel_usage * 256.9131097 * 9.9445485

    opex = fuel_costs + om_costs

    return sum_costs / sum_el_gen, initial_investment, emission_factor, opex, npc

#@jit(nopython=True)
def pv_diesel_hybrid(
        energy_per_hh,  # kWh/household/year as defined
        ghi,  # highest annual GHI value encountered in the GIS data
        ghi_curve,
        temp,
        tier,
        start_year,
        end_year,
        pv_cost_factor,
        diesel_cost=400,  # diesel generator capital cost, USD/kW rated power
        pv_no=15,  # number of PV panel sizes simulated
        diesel_no=15,  # number of diesel generators simulated
        discount_rate=0.08,
        diesel_range=[0.7]
):
    n_chg = 0.92  # charge efficiency of battery
    n_dis = 0.92  # discharge efficiency of battery
    lpsp_max = 0.10  # maximum loss of load allowed over the year, in share of kWh
    battery_cost = 311  # battery capital capital cost, USD/kWh of storage capacity
    pv_cost = 704 * pv_cost_factor  # PV panel capital cost, USD/kW peak power
    pv_life = 25  # PV panel expected lifetime, years
    diesel_life = 10  # diesel generator expected lifetime, years
    pv_om = 0.015  # annual OM cost of PV panels
    diesel_om = 0.1  # annual OM cost of diesel generator
    k_t = 0.005  # temperature factor of PV panels
    inverter_cost = 536
    inverter_life = 10
    inv_eff = 0.92  # inverter_efficiency
    charge_controller = 0

    ghi = ghi_curve * ghi * 1000 / ghi_curve.sum()
    hour_numbers = np.empty(8760)
    for i in prange(365):
        for j in prange(24):
            hour_numbers[i * 24 + j] = j
    dod_max = 0.8  # maximum depth of discharge of battery

    def load_curve(tier, energy_per_hh):
        # the values below define the load curve for the five tiers. The values reflect the share of the daily demand
        # expected in each hour of the day (sum of all values for one tier = 1)
        tier5_load_curve = [0.021008403, 0.021008403, 0.021008403, 0.021008403, 0.027310924, 0.037815126,
                            0.042016807, 0.042016807, 0.042016807, 0.042016807, 0.042016807, 0.042016807,
                            0.042016807, 0.042016807, 0.042016807, 0.042016807, 0.046218487, 0.050420168,
                            0.067226891, 0.084033613, 0.073529412, 0.052521008, 0.033613445, 0.023109244]
        tier4_load_curve = [0.017167382, 0.017167382, 0.017167382, 0.017167382, 0.025751073, 0.038626609,
                            0.042918455, 0.042918455, 0.042918455, 0.042918455, 0.042918455, 0.042918455,
                            0.042918455, 0.042918455, 0.042918455, 0.042918455, 0.0472103, 0.051502146,
                            0.068669528, 0.08583691, 0.075107296, 0.053648069, 0.034334764, 0.021459227]
        tier3_load_curve = [0.013297872, 0.013297872, 0.013297872, 0.013297872, 0.019060284, 0.034574468,
                            0.044326241, 0.044326241, 0.044326241, 0.044326241, 0.044326241, 0.044326241,
                            0.044326241, 0.044326241, 0.044326241, 0.044326241, 0.048758865, 0.053191489,
                            0.070921986, 0.088652482, 0.077570922, 0.055407801, 0.035460993, 0.019946809]
        tier2_load_curve = [0.010224949, 0.010224949, 0.010224949, 0.010224949, 0.019427403, 0.034764826,
                            0.040899796, 0.040899796, 0.040899796, 0.040899796, 0.040899796, 0.040899796,
                            0.040899796, 0.040899796, 0.040899796, 0.040899796, 0.04601227, 0.056237219,
                            0.081799591, 0.102249489, 0.089468303, 0.06390593, 0.038343558, 0.017893661]
        tier1_load_curve = [0, 0, 0, 0, 0.012578616, 0.031446541, 0.037735849, 0.037735849, 0.037735849,
                            0.037735849, 0.037735849, 0.037735849, 0.037735849, 0.037735849, 0.037735849,
                            0.037735849, 0.044025157, 0.062893082, 0.100628931, 0.125786164, 0.110062893,
                            0.078616352, 0.044025157, 0.012578616]

        if tier == 1:
            load_curve = tier1_load_curve * 365
        elif tier == 2:
            load_curve = tier2_load_curve * 365
        elif tier == 3:
            load_curve = tier3_load_curve * 365
        elif tier == 4:
            load_curve = tier4_load_curve * 365
        else:
            load_curve = tier5_load_curve * 365

        return np.array(load_curve) * energy_per_hh / 365

    load_curve = load_curve(tier, energy_per_hh)

    # This section creates the range of PV capacities, diesel capacities and battery sizes to be simulated
    ref = 5 * load_curve[19]

    battery_sizes = [0.5 * energy_per_hh / 365, energy_per_hh / 365, 2 * energy_per_hh / 365]
    pv_caps = []
    diesel_caps = []

    for i in prange(pv_no):
        pv_caps.append(ref * (pv_no - i) / pv_no)

    for j in prange(diesel_no):
        diesel_caps.append(j * max(load_curve) / diesel_no)

    #pv_caps = np.outer(np.array(pv_caps), pv_extend)
    #diesel_caps = np.outer(diesel_extend, np.array(diesel_caps))

    # This section creates 2d-arrays to store information on PV capacities, diesel capacities, battery sizes,
    # fuel usage, battery life and LPSP

    battery_size = np.ones((len(battery_sizes), pv_no, diesel_no))
    pv_panel_size = np.zeros((len(battery_sizes), pv_no, diesel_no))
    diesel_capacity = np.zeros((len(battery_sizes), pv_no, diesel_no))

    diesel_share = np.zeros((len(battery_sizes), pv_no, diesel_no))
    battery_life = np.zeros((len(battery_sizes), pv_no, diesel_no))
    lpsp = np.zeros((len(battery_sizes), pv_no, diesel_no))
    fuel_usage = np.zeros((len(battery_sizes), pv_no, diesel_no))
    excess_gen = np.zeros((len(battery_sizes), pv_no, diesel_no))

    for j in prange(len(battery_sizes)):
        battery_size[j, :, :] *= battery_sizes[j]
        pv_panel_size[j, :, :] = pv_caps
        diesel_capacity[j, :, :] = diesel_caps

    # For the number of diesel, pv and battery capacities the lpsp, battery lifetime, fuel usage and LPSP is calculated

    p = -1
    b = -1
    d = -1

    for bc in battery_sizes:
        b += 1
        p = -1
        for pc in pv_caps:
            p += 1
            d = -1
            for dc in diesel_caps:
                d += 1
                diesel_share[b][p][d], battery_life[b][p][d], lpsp[b][p][d], fuel_usage[b][p][d], excess_gen[b][p][d] = pv_diesel_capacities(pc, bc, dc, hour_numbers, temp[:, 0], ghi[:, 0], load_curve, k_t, inv_eff, n_dis, n_chg, energy_per_hh)

                battery_size[b][p][d] = bc
                pv_panel_size[b][p][d] = pc
                diesel_capacity[b][p][d] = dc


    diesel_limit = 0.5

    min_lcoe_range = []
    investment_range = []
    capacity_range = []
    ren_share_range = []
    emissions_range = []

    pv_cap_out = []
    diesel_cap_out = []
    battery_size_out = []
    battery_life_out = []
    fuel_usage_out = []
    opex_out = []
    npc_out = []

    for di in diesel_range:

        lcoe = np.zeros((len(battery_sizes), pv_no, diesel_no))
        investment = np.zeros((len(battery_sizes), pv_no, diesel_no))
        emissions = np.zeros((len(battery_sizes), pv_no, diesel_no))
        opex = np.zeros((len(battery_sizes), pv_no, diesel_no))
        npc = np.zeros((len(battery_sizes), pv_no, diesel_no))

        p = -1
        b = -1
        d = -1

        for bc in battery_sizes:
            b += 1
            p = -1
            for pc in pv_caps:
                p += 1
                d = -1
                for dc in diesel_caps:
                    d += 1

                    lcoe[b][p][d], investment[b][p][d], emissions[b][p][d], opex[b][p][d], npc[b][p][d] = calculate_hybrid_lcoe(di, end_year, start_year, energy_per_hh,
                                          fuel_usage[b][p][d], pc, pv_cost, charge_controller, pv_om, dc,
                                          diesel_cost, diesel_om, inverter_life, load_curve, inverter_cost, diesel_life, pv_life, battery_life[b][p][d],
                                          bc, battery_cost, dod_max, discount_rate)

        # lcoe, investment, emissions, opex, npc = calculate_hybrid_lcoe(d)
        lcoe = np.where(lpsp > lpsp_max, 99, lcoe)
        lcoe = np.where(diesel_share > diesel_limit, 99, lcoe)

        min_lcoe = np.min(lcoe)
        min_lcoe_combination = np.unravel_index(np.argmin(lcoe, axis=None), lcoe.shape)
        ren_share = 1 - diesel_share[min_lcoe_combination]
        capacity = pv_panel_size[min_lcoe_combination] + diesel_capacity[min_lcoe_combination]
        min_emissions = emissions[min_lcoe_combination]

        min_lcoe_range.append(min_lcoe)
        investment_range.append(investment[min_lcoe_combination])
        capacity_range.append(capacity)
        ren_share_range.append(ren_share)
        emissions_range.append(min_emissions)

        pv_cap_out.append(pv_panel_size[min_lcoe_combination])
        diesel_cap_out.append(diesel_capacity[min_lcoe_combination])
        battery_size_out.append(battery_size[min_lcoe_combination])
        battery_life_out.append(battery_life[min_lcoe_combination])
        fuel_usage_out.append(fuel_usage[min_lcoe_combination])
        opex_out.append(opex[min_lcoe_combination])
        npc_out.append(npc[min_lcoe_combination])

    return min_lcoe_range, investment_range, capacity_range, ren_share_range, emissions_range, \
           pv_cap_out, diesel_cap_out, battery_size_out, battery_life_out, fuel_usage_out, opex_out, npc_out

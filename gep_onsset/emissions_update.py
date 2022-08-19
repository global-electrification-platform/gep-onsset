import os
import shutil
import pandas as pd

SET_ELEC_FINAL_CODE = "FinalElecCode"
SET_ENERGY_PER_CELL = 'EnergyPerSettlement'
SET_POP = 'Pop'
SET_LIMIT = "ElecStatusIn"
SET_INVESTMENT_COST = 'InvestmentCost'
SET_NEW_CONNECTIONS = 'NewConnections'
SET_NEW_CAPACITY = 'NewCapacity'

countries = ['gq']
print(countries)


def calc_summaries(df, df_summary, sumtechs, year):
    """The next section calculates the summaries for technology split,
    consumption added and total investment cost"""

    # logging.info('Calculate summaries')

    # Population Summaries
    df_summary[year][sumtechs[0]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] < 3) &
                                                    (df[SET_LIMIT + "{}".format(year)] == 1)]
                                        [SET_POP + "{}".format(year)])

    df_summary[year][sumtechs[1]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 98) &
                                                    (df[SET_LIMIT + "{}".format(year)] == 1)]
                                        [SET_POP + "{}".format(year)])

    df_summary[year][sumtechs[2]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 3) &
                                                    (df[SET_LIMIT + "{}".format(year)] == 1) & (
                                                        df[SET_POP + "{}".format(year)] > 0)]
                                        [SET_POP + "{}".format(year)])

    df_summary[year][sumtechs[3]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 4) &
                                                    (df[SET_LIMIT + "{}".format(year)] == 1)]
                                        [SET_POP + "{}".format(year)])

    df_summary[year][sumtechs[4]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 8) &
                                                    (df[SET_LIMIT + "{}".format(year)] == 1)]
                                        [SET_POP + "{}".format(year)])

    df_summary[year][sumtechs[5]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 9) &
                                                    (df[SET_LIMIT + "{}".format(year)] == 1)]
                                        [SET_POP + "{}".format(year)])

    df_summary[year][sumtechs[6]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 7) &
                                                    (df[SET_LIMIT + "{}".format(year)] == 1)]
                                        [SET_POP + "{}".format(year)])

    df_summary[year][sumtechs[7]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 5) &
                                                    (df[SET_LIMIT + "{}".format(year)] == 1)]
                                        [SET_POP + "{}".format(year)])

    df_summary[year][sumtechs[8]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 6) &
                                                    (df[SET_LIMIT + "{}".format(year)] == 1)]
                                        [SET_POP + "{}".format(year)])

    # New_Connection Summaries
    df_summary[year][sumtechs[9]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] < 3) &
                                                    (df[SET_LIMIT + "{}".format(year)] == 1)]
                                        [SET_NEW_CONNECTIONS + "{}".format(year)])

    df_summary[year][sumtechs[10]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 98) &
                                                     (df[SET_LIMIT + "{}".format(year)] == 1)]
                                         [SET_NEW_CONNECTIONS + "{}".format(year)])

    df_summary[year][sumtechs[11]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 3) &
                                                     (df[SET_LIMIT + "{}".format(year)] == 1) & (
                                                         df[SET_POP + "{}".format(year)] > 0)]
                                         [SET_NEW_CONNECTIONS + "{}".format(year)])

    df_summary[year][sumtechs[12]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 4) &
                                                     (df[SET_LIMIT + "{}".format(year)] == 1)]
                                         [SET_NEW_CONNECTIONS + "{}".format(year)])

    df_summary[year][sumtechs[13]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 8) &
                                                     (df[SET_LIMIT + "{}".format(year)] == 1)]
                                         [SET_NEW_CONNECTIONS + "{}".format(year)])

    df_summary[year][sumtechs[14]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 9) &
                                                     (df[SET_LIMIT + "{}".format(year)] == 1)]
                                         [SET_NEW_CONNECTIONS + "{}".format(year)])

    df_summary[year][sumtechs[15]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 7) &
                                                     (df[SET_LIMIT + "{}".format(year)] == 1)]
                                         [SET_NEW_CONNECTIONS + "{}".format(year)])

    df_summary[year][sumtechs[16]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 5) &
                                                     (df[SET_LIMIT + "{}".format(year)] == 1)]
                                         [SET_NEW_CONNECTIONS + "{}".format(year)])

    df_summary[year][sumtechs[17]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 6) &
                                                     (df[SET_LIMIT + "{}".format(year)] == 1)]
                                         [SET_NEW_CONNECTIONS + "{}".format(year)])

    # Capacity Summaries
    df_summary[year][sumtechs[18]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] < 3) &
                                                     (df[SET_LIMIT + "{}".format(year)] == 1)]
                                         [SET_NEW_CAPACITY + "{}".format(year)])

    df_summary[year][sumtechs[19]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 98) &
                                                     (df[SET_LIMIT + "{}".format(year)] == 1)]
                                         [SET_NEW_CAPACITY + "{}".format(year)])

    df_summary[year][sumtechs[20]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 3) &
                                                     (df[SET_LIMIT + "{}".format(year)] == 1) & (
                                                         df[SET_POP + "{}".format(year)] > 0)]
                                         [SET_NEW_CAPACITY + "{}".format(year)])

    df_summary[year][sumtechs[21]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 4) &
                                                     (df[SET_LIMIT + "{}".format(year)] == 1)]
                                         [SET_NEW_CAPACITY + "{}".format(year)])

    df_summary[year][sumtechs[22]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 8) &
                                                     (df[SET_LIMIT + "{}".format(year)] == 1)]
                                         [SET_NEW_CAPACITY + "{}".format(year)])

    df_summary[year][sumtechs[23]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 9) &
                                                     (df[SET_LIMIT + "{}".format(year)] == 1)]
                                         [SET_NEW_CAPACITY + "{}".format(year)])

    df_summary[year][sumtechs[24]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 7) &
                                                     (df[SET_LIMIT + "{}".format(year)] == 1)]
                                         [SET_NEW_CAPACITY + "{}".format(year)])

    df_summary[year][sumtechs[25]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 5) &
                                                     (df[SET_LIMIT + "{}".format(year)] == 1)]
                                         [SET_NEW_CAPACITY + "{}".format(year)])

    df_summary[year][sumtechs[26]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 6) &
                                                     (df[SET_LIMIT + "{}".format(year)] == 1)]
                                         [SET_NEW_CAPACITY + "{}".format(year)])

    # Investment Summaries
    df_summary[year][sumtechs[27]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] < 3) &
                                                     (df[SET_LIMIT + "{}".format(year)] == 1)]
                                         [SET_INVESTMENT_COST + "{}".format(year)])

    df_summary[year][sumtechs[28]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 98) &
                                                     (df[SET_LIMIT + "{}".format(year)] == 1)]
                                         [SET_INVESTMENT_COST + "{}".format(year)])

    df_summary[year][sumtechs[29]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 3) &
                                                     (df[SET_LIMIT + "{}".format(year)] == 1) & (
                                                         df[SET_POP + "{}".format(year)] > 0)]
                                         [SET_INVESTMENT_COST + "{}".format(year)])

    df_summary[year][sumtechs[30]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 4) &
                                                     (df[SET_LIMIT + "{}".format(year)] == 1)]
                                         [SET_INVESTMENT_COST + "{}".format(year)])

    df_summary[year][sumtechs[31]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 8) &
                                                     (df[SET_LIMIT + "{}".format(year)] == 1)]
                                         [SET_INVESTMENT_COST + "{}".format(year)])

    df_summary[year][sumtechs[32]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 9) &
                                                     (df[SET_LIMIT + "{}".format(year)] == 1)]
                                         [SET_INVESTMENT_COST + "{}".format(year)])

    df_summary[year][sumtechs[33]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 7) &
                                                     (df[SET_LIMIT + "{}".format(year)] == 1)]
                                         [SET_INVESTMENT_COST + "{}".format(year)])

    df_summary[year][sumtechs[34]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 5) &
                                                     (df[SET_LIMIT + "{}".format(year)] == 1)]
                                         [SET_INVESTMENT_COST + "{}".format(year)])

    df_summary[year][sumtechs[35]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 6) &
                                                     (df[SET_LIMIT + "{}".format(year)] == 1)]
                                         [SET_INVESTMENT_COST + "{}".format(year)])

    # Emission Summaries
    df_summary[year][sumtechs[36]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] < 3) &
                                                     (df[SET_LIMIT + "{}".format(year)] == 1)]
                                         ['AnnualEmissions' + "{}".format(year)])

    df_summary[year][sumtechs[37]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 98) &
                                                     (df[SET_LIMIT + "{}".format(year)] == 1)]
                                         ['AnnualEmissions' + "{}".format(year)])

    df_summary[year][sumtechs[38]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 3) &
                                                     (df[SET_LIMIT + "{}".format(year)] == 1) & (
                                                         df[SET_POP + "{}".format(year)] > 0)]
                                         ['AnnualEmissions' + "{}".format(year)])

    df_summary[year][sumtechs[39]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 4) &
                                                     (df[SET_LIMIT + "{}".format(year)] == 1)]
                                         ['AnnualEmissions' + "{}".format(year)])

    df_summary[year][sumtechs[40]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 8) &
                                                     (df[SET_LIMIT + "{}".format(year)] == 1)]
                                         ['AnnualEmissions' + "{}".format(year)])

    df_summary[year][sumtechs[41]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 9) &
                                                     (df[SET_LIMIT + "{}".format(year)] == 1)]
                                         ['AnnualEmissions' + "{}".format(year)])

    df_summary[year][sumtechs[42]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 7) &
                                                     (df[SET_LIMIT + "{}".format(year)] == 1)]
                                         ['AnnualEmissions' + "{}".format(year)])

    df_summary[year][sumtechs[43]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 5) &
                                                     (df[SET_LIMIT + "{}".format(year)] == 1)]
                                         ['AnnualEmissions' + "{}".format(year)])

    df_summary[year][sumtechs[44]] = sum(df.loc[(df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 6) &
                                                     (df[SET_LIMIT + "{}".format(year)] == 1)]
                                         ['AnnualEmissions' + "{}".format(year)])



for country in countries:
    print(country)
    shutil.unpack_archive(r'C:\Users\adm.esa\Desktop\GEP_2021\{}-2\climate\results.zip'.format(country), r'C:\Users\adm.esa\Desktop\GEP_2021\{}-2\climate\results'.format(country))
    results_folder = r'C:\Users\adm.esa\Desktop\GEP_2021\{}-2\climate\results'.format(country)
    summary_folder = r'C:\Users\adm.esa\Desktop\GEP_2021\{}-2\climate\summaries'.format(country)


    scenario_info = pd.read_excel(r'C:\Users\adm.esa\Desktop\GEP_2021\emissions-2-specs.xlsx', sheet_name='ScenarioInfoAll')
    scenarios = scenario_info['Scenario']

    for scenario in scenarios:
        productive_index = scenario_info.iloc[scenario]['Productive_uses_demand']
        tier_index = scenario_info.iloc[scenario]['Target_electricity_consumption_level']
        grid_connection_index = scenario_info.iloc[scenario]['Grid_connection_cap']
        grid_generation_index = scenario_info.iloc[scenario]['Grid_electricity_generation_cost']
        pv_index = scenario_info.iloc[scenario]['PV_cost_adjust']
        rollout_index = scenario_info.iloc[scenario]['Prioritization_algorithm']

        settlements_out_csv = os.path.join(results_folder,
                                           '{}-2-{}_{}_{}_{}_{}_{}.csv'.format(country, tier_index, productive_index,
                                                                               grid_generation_index, pv_index,
                                                                               grid_connection_index, rollout_index))
        summary_csv = os.path.join(summary_folder,
                                   '{}-2-{}_{}_{}_{}_{}_{}_summary.csv'.format(country, tier_index, productive_index,
                                                                               grid_generation_index, pv_index,
                                                                               grid_connection_index, rollout_index))

        df = pd.read_csv(settlements_out_csv)
        try:
            del df['Unnamed: 0']
        except KeyError:
            pass

        df['PVHybridEmissionFactor2025'] = df['PVHybridDieselConsumption2025'] * 256.9131097 * 9.9445485 / df['EnergyPerSettlement2025']
        df['PVHybridEmissionFactor2030'] = df['PVHybridDieselConsumption2030'] * 256.9131097 * 9.9445485 / df['EnergyPerSettlement2030']

        df['WindHybridEmissionFactor2025'] = df['WindHybridDieselConsumption2025'] * 256.9131097 * 9.9445485 / df['EnergyPerSettlement2025']
        df['WindHybridEmissionFactor2030'] = df['WindHybridDieselConsumption2030'] * 256.9131097 * 9.9445485 / df['EnergyPerSettlement2030']

        for year in [2025, 2030]:
            df.loc[df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 5, 'AnnualEmissions' + "{}".format(year)] = df[SET_ENERGY_PER_CELL + "{}".format(year)] * df['PVHybridEmissionFactor' + "{}".format(year)] / 1000
            df.loc[df[SET_ELEC_FINAL_CODE + "{}".format(year)] == 6, 'AnnualEmissions' + "{}".format(year)] = df[SET_ENERGY_PER_CELL + "{}".format(year)] * df['WindHybridEmissionFactor' + "{}".format(year)] / 1000

        df['AnnualEmissionsTotal'] = df['AnnualEmissions' + "{}".format(2030)] + df['AnnualEmissions' + "{}".format(2025)]

        yearsofanalysis = [2025, 2030]
        elements = ["1.Population", "2.New_Connections", "3.Capacity", "4.Investment", "5.Emissions"]
        techs = ["Grid", "SA_Diesel", "SA_PV", "MG_Diesel", "MG_PV", "MG_Wind", "MG_Hydro", "MG_PV_Hybrid",
                 "MG_Wind_Hybrid"]
        sumtechs = []
        for element in elements:
            for tech in techs:
                sumtechs.append(element + "_" + tech)
        total_rows = len(sumtechs)
        df_summary = pd.DataFrame(columns=yearsofanalysis)
        for row in range(0, total_rows):
            df_summary.loc[sumtechs[row]] = "Nan"
        
        for i in range(len(df.columns)):
            if df.iloc[:, i].dtype == 'float64':
                df.iloc[:, i] = pd.to_numeric(df.iloc[:, i], downcast='float')
            elif df.iloc[:, i].dtype == 'int64':
                df.iloc[:, i] = pd.to_numeric(df.iloc[:, i], downcast='signed')

        for year in yearsofanalysis:
             calc_summaries(df, df_summary, sumtechs, year)

        df_summary.to_csv(summary_csv, index=sumtechs)
        df.to_csv(settlements_out_csv, index=False)

    shutil.make_archive(results_folder, 'zip', results_folder)
    shutil.make_archive(summary_folder, 'zip', summary_folder)

    shutil.rmtree(results_folder)
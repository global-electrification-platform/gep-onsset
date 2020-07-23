Scenario run
=================================

If the previous steps have been succesful, running an electrification scenario with **gep_onsset** is a fairly straightforward process. 

Running with GEP Generator
*******************************

The simplest way to run a scenario is via ``GEP Generator.ipynb``. You may refer to the previous section on how to get is up running. In order to run a scenario you will need:

- **The primary input file** (see *Malawi.csv* from previous section)
- **Fill in the calibration parameters** (see *Steps 2,4, 5* from previous section)
- **Provide the scenario parameters** (*Steps 3 & 6*)

.. note::
	There are 6 scenario parameters in *Step 3* - also called "levers" in the GEP ecosystem. Each lever has 1-3 possible options the combination of which can generate 216 scenario as presented in the `GEP Explorer <https://electrifynow.energydata.info/>`_. The GEP generator guides the selection process with embedded documentation and link to the relevant sources.

**Step 7** runs the electrification analysis for the specified scenario. **Note** that in this step, you may also provide the parameter `cost_choice` if you want to include (1) or exclude (2) break down of investment costs. The first option will add computational time in the analysis.

**Step 8** prepares a summary table, four graphs and a map over the key results of the analysis for a quick, on-the-fly review. 

**Step 9** expoprts the results into 3 csv files. The **_Variables**.csv file provides a summary of input variables. The **_Summaries**.csv file provides a summary of key results of the electrification analysis. The **_Results**.csv file provides the electrification results in full granularity. An overview of the content is available in the next section.


Running with gep_runner
*******************************
The **gep_runner** is usually used to run multiple scenarios at once. As shown in the previous section, interaction with the code takes place in the python console. Upon initiation, you may select option 3 for scenario run(s).

- 1: To split countries in case of multiple country runs (used rarely)
- 2: To prepare/calibrate the GIS input file
- **3: To run scenario(s)**

.. note::
	**Note** that in the latest update, you will also be prompted to provide the parameter `cost_choice` if you want to include (1) or exclude (2) break down of investment costs. The first option will add computational time in the analysis.

Execution requires two files:

- **The specs file** (see previous section)
- **The calibrated input file** (see from previous section)

Scenario definition is possible in the ``ScenarioInfo`` sheet of the specs file. There one can parameterize the "levers" accordingly and create a bundle of scenarios. Each row represents one potential scenario. The **gep_runner** will run as many scenarios as defined in this sheet. 

The following table gives on overview of the potential scenario combinations.

+--------------------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Lever                                | Option  | Description                                                                                                                                                   |
+======================================+=========+===============================================================================================================================================================+
| Population_Growth                    |   0, 1  | Expected population in the country by the end year of the analysis; 0:   low population growth, 1: high population growth                                     |
+--------------------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Target_electricity_consumption_level | 0, 1, 2 | 0: low electricity demand target (e.g. U4R1), 1: high electricity demand   target (e.g. U5R3), 2: use the custom residential demand target layer (from   GIS) |
+--------------------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Electrification_target_5_years       |   0, 1  | 0: low electrification target in the intermediate year (e.g. 35%), 1:   high electrification target in the intermediate year (e.g. 60%)                       |
+--------------------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Grid_electricity_generation_cost     |   0, 1  | 0: low generating cost for the grid (e.g. 0.03), 1: high generating cost   for the grid (e.g. 0.08)                                                           |
+--------------------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| PV_cost_adjust                       | 0, 1, 2 | 0: PV capacity cost as defined by the user, 1: PV capacity cost reduced   by 25%, 2: PV capacity cost increased by 25%                                        |
+--------------------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Diesel_price                         |   0, 1  | 0: low diesel price , 1: high diesel price                                                                                                                    |
+--------------------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Productive_uses_demand               |   0, 1  | 0: not including productive uses of electricity, 1: including productive   uses of electricity                                                                |
+--------------------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Prioritization_algorithm             | 0, 1, 2 | 0: least cost prioritization, 1: forced grid within 1km, 2: forced grid   within 2km                                                                          |
+--------------------------------------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

Therefore the scenario ``0_0_0_0_0_0`` will respectively represent:

- low population growth
- low electricity demand target (e.g. U4R1)
- low electrification target in the intermediate year (e.g. 35%)
- low generating cost for the grid (e.g. 0.03)
- PV capacity cost as defined by the user
- low diesel price
- not including productive uses of electricity
- least cost prioritization

**Note** that in the ``ScenarioParameters`` sheet one can customize how the aforementioned codes are translated to tangible input variables in the **gep_onsset** code.

The **gep_runner** yields two csv files for each scenario. 

- The **_Summaries**.csv file that provides a summary of key results of the electrification analysis and 
- The **_Results**.csv file that provides the electrification results in full granularity 

An overview of the content is available in the next section.

.. note::
	The scenario coding convention is applied in the naming process of the output result files as well. For example the same scenario for Malawi would yield the result file names ``mw-1-0_0_0_0_0_0.csv``.

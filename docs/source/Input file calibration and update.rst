Input file calibration and update
=================================

The primary input file (see previous section) includes rough data as extracted from the GIS layers. Before proceeding with the electrification analysis, these values need to be conditioned and/or calibrated.

**Conditioning** makes sure that physical values (e.g. GHI, Wind speed, land cover, elevation etc.) are within acceptable limits. 

**Calibration** makes sure some of the parameters (e.g. total population, urban/rural ration, electrification rate etc.) are in line with official statistics.

 **New columns** are also created and support later stages of the analysis (e.g. wind capacity factor, grid penalty ratio, electrification status etc.).

Calibration with gep_runner
*******************************
The **gep_runner.py** is used to call functions from the **gep_onsset.py** as requested. You may execute **gep_runner** in any IDE of preference, we suggest PyCharm.

Interaction with the code using **gep_runner** takes place in the python console or your IDE. Upon initiation, the code will prompt you to select one of the three following options:

- 1: To split countries in case of multiple country runs (used rarely)
- **2: To prepare/calibrate the GIS input file**
- 3: To run scenario(s)

For calibration you may select option 2. Execution requires two files:

- **The primary input file** (see *Malawi.csv* from previous section)
- **The specs file** (see example of `specs_mw_one_scenario.csv <https://github.com/global-electrification-platform/gep-onsset/tree/master/test_data>`_). 

The specs file contains the parameters and their values against which the GIS data are conditioned or calibrated. The user shall fill in all necessary values in the `SpecsData` sheet. A description of the parameters is presented below.

+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--+
| Parameter                              | Description                                                                                                                                                       |  |
+========================================+===================================================================================================================================================================+==+
| Country                                | Name of the country                                                                                                                                               |  |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--+
| CountryCode                            | ALPHA-2 country code as per ISO 3166 international standard                                                                                                       |  |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--+
| StartYear                              | Base year of the analysis; usually selected based on data availability                                                                                            |  |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--+
| EndYEar                                | End year of the analysis                                                                                                                                          |  |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--+
| PopStartYear                           | Official population at the base year                                                                                                                              |  |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--+
| UrbanRatioStartYear                    | Official urban population ratio in the base year                                                                                                                  |  |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--+
| UrbanCutOff                            | Population threshold above which a settlement can be considered urban   (optional)                                                                                |  |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--+
| UrbanRatioModelled                     | This value is provided by the model after calibration                                                                                                             |  |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--+
| PopEndYearHigh                         | Expected population at the end year based on high growth rate                                                                                                     |  |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--+
| PopEndYearLow                          | Expected population at the end year based on high growth rate                                                                                                     |  |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--+
| UrbanRatioEndYear                      | Expected urban population ration in the end year                                                                                                                  |  |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--+
| NumPeoplePerHHRural                    | Number of people per household - rural settlements                                                                                                                |  |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--+
| NumPeoplePerHHUrban                    | Number of people per household - urban settlements                                                                                                                |  |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--+
| GridCapacityInvestmentCost             | Expected investment cost per kW of additional capacity in the central   grid system                                                                               |  |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--+
| GridLosses                             | Expected transmission ans distribution losses in the grid network                                                                                                 |  |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--+
| BaseToPeak                             | Average to peak load ratio for the grid; used for sizing additional   capacity due grid extension and to accommodate reliability issues                           |  |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--+
| ExistingGridCostRatio                  | Persentage of capital cost increase in each grid extension iteration;   used to accommodate reinforcement of grid and reliability of supply                       |  |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--+
| MaxGridExtensionDist                   | Maximum distance (in km) that MV lines can reach in each iteration loop                                                                                           |  |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--+
| NewGridGenerationCapacityAnnualLimitMW | Capacity that can be added to the central grid per year of analysis                                                                                               |  |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--+
| ElecActual                             | Official national electrification rate in the base year                                                                                                           |  |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--+
| Rural_elec_ratio                       | Official national electrification rate in rural areas in the base year                                                                                            |  |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--+
| Urban_elec_ratio                       | Official national electrification rate in urban areas in the base year                                                                                            |  |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--+
| ElecModelled                           | This value is provided by the model after calibration                                                                                                             |  |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--+
| urban_elec_ratio_modelled              | This value is provided by the model after calibration                                                                                                             |  |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--+
| rural_elec_ratio_modelled              | This value is provided by the model after calibration                                                                                                             |  |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--+
| MinNightLights                         | Nighttime light value above which a settlement can be consedered   electrified; used to identify and calibrate electrification rate in the base   year            |  |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--+
| DistToTrans                            | Distance to transformers (in km) above which a settlement can be   consedered electrified; used to identify and calibrate electrification rate   in the base year |  |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--+
| MaxGridDist                            | Distance to T&D network (in km) above which a settlement can be   consedered electrified; used to identify and calibrate electrification rate   in the base year  |  |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--+
| MaxRoadDist                            | Distance to road network (in km) above which a settlement can be   consedered electrified; used to identify and calibrate electrification rate   in the base year |  |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--+
| PopCutOffRoundOne                      | This value is provided by the model after calibration                                                                                                             |  |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--+
| PopCutOffRoundTwo                      | This value is provided by the model after calibration                                                                                                             |  |
+----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+--+

.. note::

    With **gep_runner** the calibration process runs only once. The process finishes once the conditioning and calibration is complete and the result is a "calibrated" csv file. The user might check the result file and the specs file, which has updated some of the parameters and decide whether the result is satisfactory or the process requires modification.  

Calibration with GEP Generator
*******************************
The GEP Generator is an interactive interface, developed as a jupyter notebook (.ipynb) in order to support calling functions in the **gep_onsset** model. The GEP Generator is located in the root directory of the repository. You may access it by simply navigating there via anaconda prompt using:

``> cd ..\my_designated_local_directory``

``..\my_designated_local_directory> jupyter notebook`` 

Jupyter notebook will open on your default browser; simply select to open the ``GEP Generator.ipynb`` and you are set to go!

The GEP Generator runs in 9 steps. **Step 1**, requires that the user provides the primary input file (see previous section). **Steps 2 & 4** replace the specs file and allow the user to provide the calibrating parameters in real time. **Step 5** conducts the conditioning and calibration process. 

.. note::
	Note that the GEP generator **does not** store the calibrated results in a separate file but rather continues right away to the scenario runs. This makes the process faster on the one hand, but it means that the conditioning and calibration process runs anew everytime a scenario is executed (only one at a time). 

Example of the calibrated input file
*************************************

The calibration process will add the following columns to the input file.

+----+-------------------------------------+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|  # | Column                              |     Unit     | Description                                                                                                                                                                                                                            |
+====+=====================================+==============+========================================================================================================================================================================================================================================+
| 39 | PopStartYear                        |    people    | Calibrated population to match with official statistics in the   base year                                                                                                                                                             |
+----+-------------------------------------+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 40 | Pop<year>High                       |    people    | Projected population in the specified <year> based on   high growth indicators; for intermediate and end years                                                                                                                         |
+----+-------------------------------------+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 41 | Pop<year>Low                        |    people    | Projected population in the specified <year> based on   low growth indicators; for intermediate and end years                                                                                                                          |
+----+-------------------------------------+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 42 | Pop<base year>                      |    people    | Calibrated population to match with official statistics in the   base year                                                                                                                                                             |
+----+-------------------------------------+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 43 | RoadDistClassified                  |    1 to 5    | Classified value of distance to road used to calculate grid   penalty factor                                                                                                                                                           |
+----+-------------------------------------+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 44 | SubstationDistClassified            |    1 to 5    | Classified value of distance to sub-station used to calculate   grid penalty factor                                                                                                                                                    |
+----+-------------------------------------+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 45 | LandCoverClassified                 |    1 to 5    | Classified value of land cover type used to calculate grid   penalty factor                                                                                                                                                            |
+----+-------------------------------------+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 46 | ElevationClassified                 |    1 to 5    | Classified value of elevation used to calculate grid penalty   factor                                                                                                                                                                  |
+----+-------------------------------------+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 47 | SlopeClassified                     |    1 to 5    | Classified value of slope used to calculate grid penalty   factor                                                                                                                                                                      |
+----+-------------------------------------+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 48 | GridClassification                  |    1 to 5    | Grid extension suitability index; Higher value indicates   higher suitability; based on an Analytic Hierarchy Process (AHP) over the   above parameters                                                                                |
+----+-------------------------------------+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 49 | GridPenalty                         |    number    | Grid extension cost multiplier based on above classification;   default value 1 induces no additional costs                                                                                                                            |
+----+-------------------------------------+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 50 | WindCF                              | from ~0 to 1 | Wind capacity factor estimated based on available wind speed   and power rating of Vestas V-44 600kW turbine                                                                                                                           |
+----+-------------------------------------+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 51 | ElecPopCalib                        |    people    | Number of people with access to (grid) electricity, calibrated   to match official statistics in the base year                                                                                                                         |
+----+-------------------------------------+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 52 | ElecStart                           |      0,1     | Electrification status in the base year; 0: non-electrified 1:   electrified (by the grid)                                                                                                                                             |
+----+-------------------------------------+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 53 | GridDistCalibElec                   |      km      | Distance to nearest power infrastructure element (transformer,   MV, HV); based on their availability. In case transformers are not available   it will lookup the next available element (e.g. MV)                                    |
+----+-------------------------------------+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 54 | Elec_Initial_Status_Grid<base year> |      0,1     | Grid electricity status in the specified base year; 0:   non-electrified 1: electrified by the grid                                                                                                                                    |
+----+-------------------------------------+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 55 | Elec_Init_Status_Offgrid<base year> |      0,1     | Off-grid electricity status in the specified base year; 0:   non-electrified 1: electrified by an off-grid technology                                                                                                                  |
+----+-------------------------------------+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 56 | Actual_Elec_Status_<base year>      |      0,1     | Overall electrification status in the specified year; 0:   non-electrified 1: electrified by any technology                                                                                                                            |
+----+-------------------------------------+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 57 | FinalElecCode<base year>            | 1 to 8 or 99 | Code of electrifying technology in the specified year (1:   grid, 2: stand-alone diesel, 3: stand-alone PV, 4: Mini-grid diesel, 5:   Mini-grid PV, 6: Mini-grid Wind, 7: Mini-grid Hydro, 8: Hybrid Mini-grid, 99:   not-electrified) |
+----+-------------------------------------+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 58 | GridReachYear                       |     year     | Estimated year that the grid might be able to reach this   settlement; currently de-activated and not used in the GEP                                                                                                                  |
+----+-------------------------------------+--------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

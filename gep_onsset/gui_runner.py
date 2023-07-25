"""Provides a GUI for the user to choose input files

This file runs either the calibration or scenario modules in the runner file,
and asks the user to browse to the necessary input files
"""

import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from runner import calibration, scenario
import os
import shutil
import time

root = tk.Tk()
root.withdraw()
root.attributes("-topmost", True)

choice = int(input('Enter 1 to prepare/calibrate the GIS input file, 2 to run scenario(s): '))

countries = ['bj']

print(countries)

#messagebox.showinfo('OnSSET', 'Open the specs file')
#specs_path = filedialog.askopenfilename()
#specs = pd.read_excel(specs_path, index_col=0)

for country in countries:


    if choice == 1:
        messagebox.showinfo('OnSSET', 'Open the file containing separated countries')
        csv_path = filedialog.askopenfilename()

        specs_path = r'C:\Users\adm.esa\Desktop\GEP_2021\{}-2\inputs\{}-2-specs.xlsx'.format(country, country)
        specs = pd.read_excel(specs_path, index_col=0)

        csv_path = r'C:\Users\adm.esa\Desktop\GEP_2021\{}-2\{}-2-country-inputs-uncalibrated.csv'.format(country, country)

        messagebox.showinfo('OnSSET', 'Browse to result folder and name the calibrated file')
        calibrated_csv_path = filedialog.asksaveasfilename()
        calibrated_csv_path = calibrated_csv_path + '.csv'

        messagebox.showinfo('OnSSET', 'Browse to result folder and name the calibrated specs file')
        specs_path_calib = filedialog.asksaveasfilename()
        specs_path_calib = specs_path_calib + '.xlsx'

        calibration(specs_path, csv_path, specs_path_calib, calibrated_csv_path)

    elif choice == 2:
        # messagebox.showinfo('OnSSET', 'Open the csv file with calibrated GIS data')
        # calibrated_csv_path = filedialog.askopenfilename()

        calibrated_csv_path = r'C:\Users\adm.esa\Desktop\GEP_2021\{}-2\climate\{}-2-country-inputs-2023.csv'.format(country, country)

        specs_path = r'C:\Users\adm.esa\Desktop\GEP_2021\00_climate_specs\{}-3-specs.xlsx'.format(country, country)

        # messagebox.showinfo('OnSSET', 'Open the file with hourly PV data')
        # pv_path = filedialog.askopenfilename()
        #
        # messagebox.showinfo('OnSSET', 'Open the file with hourly Wind data')
        # wind_path = filedialog.askopenfilename()
        #
        # print(calibrated_csv_path)
        # messagebox.showinfo('OnSSET', 'Browse to RESULTS folder to save outputs')
        # results_folder = filedialog.askdirectory()
        #
        # messagebox.showinfo('OnSSET', 'Browse to SUMMARIES folder and name the scenario to save outputs')
        # summary_folder = filedialog.askdirectory()

        # try:
        #     os.makedirs(r'C:\Users\adm.esa\Desktop\GEP_2021\{}-2\climate\{}-3-scenarios-results'.format(country, country))
        # except FileExistsError:
        #     pass
        # results_folder = r'C:\Users\adm.esa\Desktop\GEP_2021\{}-2\climate\{}-3-scenarios-results'.format(country, country)
        #
        # try:
        #     os.makedirs(r'C:\Users\adm.esa\Desktop\GEP_2021\{}-2\climate\{}-3-scenarios-summaries'.format(country, country))
        # except FileExistsError:
        #     pass
        # summary_folder = r'C:\Users\adm.esa\Desktop\GEP_2021\{}-2\climate\{}-3-scenarios-summaries'.format(country, country)

        results_folder = r'C:\Users\adm.esa\Desktop\GEP_2021\00_Climate_Test'
        summary_folder = r'C:\Users\adm.esa\Desktop\GEP_2021\00_Climate_Test\summaries'

        pv_path = r'C:\Users\adm.esa\Desktop\GEP_2021\{}-2\inputs\{}-2-pv.csv'.format(country, country)
        wind_path = r'C:\Users\adm.esa\Desktop\GEP_2021\{}-2\inputs\{}-2-wind.csv'.format(country, country)

        scenario(specs_path, calibrated_csv_path, results_folder, summary_folder, pv_path, wind_path)

print('Finished', time.ctime())
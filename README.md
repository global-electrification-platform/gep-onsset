gep_onsset
=================================

[![Documentation Status](https://readthedocs.org/projects/gep-onsset/badge/?version=latest)](https://gep-onsset.readthedocs.io/en/latest/?badge=latest)

Documentation: https://gep-onsset.readthedocs.io/en/latest/index.html#

# Scope

This repository contains the modified source code of the Open Source Spatial Electrification Tool ([OnSSET](http://www.onsset.org/)) that was developed to support the functionalities of the [Global electrification Platform](https://electrifynow.energydata.info/).

## Content

- **gep_onsset.py**: the modified source code of the OnSSET model used in the GEP
- **GEP Generator.ipynb** user-friendly scenario runner developed as a jupyter notebook for easy replication of GEP Explorer scenarios
- **gep_runner.py**: scenario runner using IDE console preferred for for stand alone calibration and/or multiple scenario runs
- **test_data** directory condains input data files for testing:
    - Malawi.csv (primary input file)
    - specs_mw_one_scenario.xlsx (specs file)
- **sample_output** directory contains indicative results of the electrification model
    - mw-1-0_0_0_0_0_1.csv (sample full result file)
    - mw-1-0_0_0_0_0_1_summary.csv (sample summary result file)
- **docs** directory contains supporting project documentation
- **gep_onsset_env.yml** environment info for setting up package requirements related for all supporting processes in this repository

More information on how to replicate, run and interprate results are available in [user's guide.](https://gep-onsset.readthedocs.io/en/latest/index.html#)

## Contact
For any questions, feedback or general inquiries please to not hesitate to contact the development team.

**The World Bank**

- Benjamin Stewart <bstewart@worldbankgroup.org>
- Alexandros Korkovelos <akorkovelos@worldbank.org>

**KTH dES**

- Andreas Sahlberg <asahl@kth.se>
- Babak Khavari <khavari@kth.se>

For any other inquiries and potential collaboration please refer to http://electrifynow.energydata.info

gep_onsset
=================================

[![Documentation Status](https://readthedocs.org/projects/gep-onsset/badge/?version=latest)](https://gep-onsset.readthedocs.io/en/latest/?badge=latest)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/global-electrification-platform/gep-onsset/HEAD)

Documentation: https://gep-onsset.readthedocs.io/en/latest/index.html#

# Scope

This repository contains the modified source code of the Open Source Spatial Electrification Tool ([OnSSET](http://www.onsset.org/)) that was developed to support the functionalities of the [Global electrification Platform](https://electrifynow.energydata.info/).

## Content

- **onsset.py**: the modified source code of the OnSSET model used in the GEP
- **GEP Generator.ipynb** user-friendly scenario runner developed as a jupyter notebook for easy replication of GEP Explorer scenarios
- **runner.py**: scenario runner using IDE console preferred for for stand alone calibration and/or multiple scenario runs
- **test_data** directory condains input data files for testing:
    - sl-2-country-inputs-calibrated.csv (primary input file for Sierra Leone-- calibrated)
    - sl-2-specs_calibrated.xlsx (specs file for Sierra Leone -- after calibration)
- **sample_output** directory contains indicative results of the electrification model
    - sl-2-1_0_0_0_0_1.csv (sample full result file for Sierra Leone)
    - sl-2-1_0_0_0_0_1_summary.csv (sample summary result file for Sierra Leone)
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

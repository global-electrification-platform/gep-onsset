Preparation of the primary input file
======================================

Q-GIS plug-in for developing population clusters
*************************************************************

The identification of population settlements is the basis of the electrification analysis in many models.
**gep_onsset** requires that population settlements are represented as vector clusters. KTH dESA has developed a methodology for generating such vector clusters based on open access data. The `output dataset <https://data.mendeley.com/datasets/z9zfhzk8cr/3>`_ is openly accessible. Furthermore, an open source `Q-GIS plug-in <https://github.com/global-electrification-platform/Clustering>`_.

.. note::  The above methodology requires processing in `Q-GIS <https://www.qgis.org/en/site/>`_ (an open-source GIS software).


Q-GIS plug-in for extracting GIS information to vector clusters
********************************************************************

Geospatial electrification models are inextricably connected with GIS data. Extracting geospatial information to each vector cluster (see above), is therefore a necessary yet time consuming process. The extraction commands can be executed manually in QGIS; however, the KTH team has developed a 
`Q-GIS plugin <https://github.com/global-electrification-platform/Cluster-based_extraction_OnSSET>`_ in order to automate the process.

.. note::  In order to run succelfully run **gep_onsset** the vector clusters need to be attributed using 26 GIS layers. An extensive list of those together with open access sources is available `here <https://drive.google.com/file/d/1O3N1vrGJtLEPN4_3_KxJDxqc4cCEo2H9/view?usp=sharing>`_.

Training material
#############################
Training material related to the use of gep_onsset package are available on `Google's Open Online Education platform <https://gep-education-demo.appspot.com/gep_training/course>`_.
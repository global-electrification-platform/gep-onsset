Software installation
=====================

**gep_onsset.py** contains all the functions needed to prepare and run a GIS based electrification analysis. It is therefore important that the module is installed and set up properly on your local machine. The following paragraphs provide all information needed to get you started!


Install from GitHub
######################

Access the `gep_onsset <https://github.com/global-electrification-platform/gep-onsset>`_ repository on GitHub. Download the zipped repository directly or clone it to you designated local directory. The latter requires that `git <https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>`_ is installed in your machine. To clone the repo you may use the following command: 

``git clone https://github.com/global-electrification-platform/gep-onsset.git``


Requirements & Working environment
#######################################
**gep_onsset.py** (as well as all supporting scripts in this repo) have been developed in Python 3. We recommend installing `Anaconda free distribution <https://www.anaconda.com/>`_ as suited for your operating system. 

Once installed, you may open anaconda prompt and set up the working environment. The **gep_onsset_env.yml** file - located in the root directory of the repository - contains all necessary packages. You may use it to set up a new virtual environment by using:

``conda env create --name gep_onsset_env --file gep_onsset_env.yml``

This might take a while.. When complete, activate the virtual environment using:

``conda activate gep_onsset_env`` 

Now you are set to begin exploring the model!

Python Interfaces & IDEs
###############################
Integrated Development Environments are used in order to ease the programming process when multiple or long scripts are required. They allow the user to interact with the code (e.g. call functions, apply changes etc.).

**Jupyter notebook (via Anaconda)**
*************************************
Jupyter notebook is a console-based, interactive computing approach providing a web-based application suitable for capturing the whole computation process: developing, documenting, and executing code, as well as communicating the results. Jupyter notebook is for example used for the GEP_generator interface. 

**PyCharm**
********************
For additional experimentation with the code one might prefer to use another IDE. While there are plenty of IDEs developed for Python, we suggest `PyCharm <https://www.jetbrains.com/pycharm/>`_ Community version as it is a well-known, open access IDE. 

Both of the above are described in more detail in the **scenario_run_reference** section.

Additional Info
###################

* Basic `navigating commands for DOS (cmd) <https://community.sophos.com/kb/en-us/13195>`_
* Git `Cheat Sheet <https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf>`_
* `Modules <https://docs.python.org/3/installing/index.html>`_
  and `packages <https://packaging.python.org/tutorials/installing-packages/>`_
  installation documentation from python.org
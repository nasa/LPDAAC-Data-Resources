# Repository Setup Instructions

The tutorials and how-tos in all repositories developed by LP DAAC team require a compatible Python Environment, an installation of [Git](https://git-scm.com/downloads). See details on prerequisites and Environment Setup instructiones below. 

---

## 1. Prerequisites

+ To access or download NASA Earth data, a `.netrc` file with your NASA Earthdata Login information is needed. You can created an account [here](https://urs.earthdata.nasa.gov/users/new) if you do not have one. You can manually create a `.netrc` file but `earthaccess.login(persist=True)` function will prompt for your NASA Earthdata username and password to create one if one does not exist and then uses your account information for  authentication purposes. 

+ Install Environment Manager:
  
  + If you do not have an Environment Manager installed, we recommend [mamba](https://mamba.readthedocs.io/en/latest/) to manage Python packages.
    + To install *mamba*, download [mambaforge](https://github.com/conda-forge/miniforge#mambaforge) for your operating system. If using Windows, be sure to check the box to "Add mamba to my PATH environment variable" to enable use of mamba directly from your command line interface. 
  

  + If prefer *conda* Environment Manager, install [Anaconda](https://www.anaconda.com/products/distribution) or [miniconda](https://docs.conda.io/en/latest/miniconda.html). When installing, Anaconda or Miniconda be sure to check the box to "Add Anaconda to my PATH environment variable" to enable use of conda directly from your command line interface. [Additional information](https://conda.io/docs/user-guide/tasks/manage-environments.html) on setting up and managing Conda environments.  

    + *mamba* typically offers higher speed and more reliable environment solutions. You still can utilize *mamba* with *conda* to manage packages. To install mamba, use your preferred command line interface (command prompt, terminal, cmder, etc.) and type the following:
        > `conda install mamba -n base -c conda-forge` 

    See more details on installation of *mamba* [here](https://mamba.readthedocs.io/en/latest/mamba-installation.html#mamba-install). 
    **Note that this may cause an issue if you have an existing mamba install through Anaconda.** 
    

+ If you do not have Git, you can download it [here](https://git-scm.com/downloads). 
 

## 2. Python Environment Setup  

This Python Environment will work for all tutorials developed by LP DAAC team existing within this repository in additione to Resource Repository directed to from this repository.  All required packages are included in an `.yml` file stored in `setup` folder. Using your preferred command line interface (command prompt, terminal, cmder, etc.) type the following to create a compatible Python environment:


+ For Windows:  

> `mamba env create -f python/setup/lp_tutorials_windows.yml`  

+ For MacOS:

> `mamba env create -f setup/lp_tutorials_macos.yml`

**If you are using *conda*, replace the "mamba" with "conda".**

## 2. Opening the notebooks

If you did the above and already have your environment activated, you can simply launch Jupyter Notebook by typing the following in command line:

> `jupyter notebook`

If returning to an already created but inactive environment, using your preferred command line interface (command prompt, terminal, cmder, etc.) navigate to your local copy of the repository, then type the following to activate the Python Environment:

> `mamba activate lp_tutorials`  

Now you can launch Jupyter Notebook to open the notebooks included.

> `jupyter notebook`  



**Still having trouble getting a compatible Python environment set up? Contact [LP DAAC User Services](https://lpdaac.usgs.gov/lpdaac-contact-us/).**  

## Contact Info  

Email: <LPDAAC@usgs.gov>  
Voice: +1-866-573-3222  
Organization: Land Processes Distributed Active Archive Center (LP DAAC)¹  
Website: <https://lpdaac.usgs.gov/>  
Date last modified: 08-25-2023  

¹Work performed under USGS contract G15PD00467 for NASA contract NNG14HH33I.  

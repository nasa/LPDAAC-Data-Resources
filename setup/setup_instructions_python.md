# Repository Setup Instructions

The tutorials and how-tos in all repositories developed by LP DAAC team require a compatible Python Environment, an installation of [Git](https://git-scm.com/downloads). See details on prerequisites and Python environment Setup instructions below. 

---

## 1. Prerequisites

+ To access or download NASA Earth data, a `.netrc` file with your NASA Earthdata Login information is needed. You can create an account [here](https://urs.earthdata.nasa.gov/users/new) if you do not have one. You can manually create a `.netrc` file but `earthaccess.login(persist=True)` function will prompt for your NASA Earthdata username and password to create one if one does not exist and then uses your account information for  authentication purposes. 

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

This Python environment will work for all tutorials developed by LP DAAC team existing within this repository in addition to Resource Repository directed to from this repository.  All required packages are included in an `.yml` file stored in `setup` folder. Using your preferred command line interface (command prompt, terminal, cmder, etc.) follow the steps below to create a compatible Python environment.

Type the following in the command line and press enter to create a compatible environment with the most updated packages.
> `mamba env create -f setup/lp_tutorials.yml`  

**If you are using *conda*, replace the "mamba" with "conda" and be patient.**

To reproducible the exact Python environment that all tutorials are tested with follow the steps below. `conda-lock` and `micromamba` both can be used to generate a conda environments using a lock file. `micromamba` is a tiny version of the mamba package manager and could speed up the installation. 

- To create a Python environment using **conda-lock**:
  - First, type the following in the command line to install `conda-lock`:
    > `conda install --channel=conda-forge --name=base conda-lock`
    - For more details on how to install `conda-lock` visit https://github.com/conda/conda-lock#installation. 
`   
  - Next, create the environment using the `conda-lock.yml` file stored in `setup` folder.
    >  `conda-lock install --name ENV_NAME setup/conda-lock.yml`
    - make sure to include the 

- To create a Python environment using **micromamba**:
  - First, type the following in the command line to install `micromamba`:
    > `conda install -c conda-forge micromamba`
    - For more details on how to install `micromamba` visit https://mamba.readthedocs.io/en/latest/micromamba-installation.html#. 

  - Next, create the environment using the `conda-lock.yml` file stored in `setup` folder.
    > `micromamba create -n ENV_NAME -f setup/conda-lock.yml`


## 3. Opening the notebooks

If you did the above and already have your environment activated, you can simply launch Jupyter Notebook by typing the following in command line:

> `jupyter notebook`

If returning to an already created but inactive environment, using your preferred command line interface (command prompt, terminal, cmder, etc.) navigate to your local copy of the repository, then type the following to activate the Python Environment:

> `mamba activate lpdaac`  

Now you can launch Jupyter Notebook to open the notebooks included.

> `jupyter notebook`  

**Still having trouble getting a compatible Python environment set up? Contact [LP DAAC User Services](https://lpdaac.usgs.gov/lpdaac-contact-us/).**  

## Contact Info  

Email: <LPDAAC@usgs.gov>  
Voice: +1-866-573-3222  
Organization: Land Processes Distributed Active Archive Center (LP DAAC)¹  
Website: <https://lpdaac.usgs.gov/>  
Date last modified: 09-27-2023  

¹Work performed under USGS contract G15PD00467 for NASA contract NNG14HH33I.  



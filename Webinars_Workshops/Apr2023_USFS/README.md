# Hands-on Workshop for Accessing, Processing, and Analyzing GEDI Data
---

## Description:

These materials were presented at the `USFS - NASA JOINT APPLICATIONS WORKSHOP`  on Tuesday, April 25, 2023 . LP DACC will presend in collaboration with ORNL DAAC. The goal  of this 30 minutes talk is to provide participants with information and resources for downloading and working with GEDI data using NASA's Earthdata Search Client and Python. This repository contains all of the materials used during this workshop.   
***  
---
## Topics Covered:

**1. Introduction to GEDI Data**    
**2. Search and Download GEDI Data Using Earthdata Search Client**    
**3. Work with GEDI data using Python** 

---
## Prerequisites/Setup Instructions

### Repository Setup Instructions

The notebook in this repository require a compatible Python Environment and installation of [Git](https://git-scm.com/downloads). You also may need to download a GEDI granule. To setup the environment and download the granule, follow the steps below. 

+ If you do not have Git, you can download it [here](https://git-scm.com/downloads).  

---
### 1. Environment Setup

It is recommended to use Conda, an environment manager to set up a compatible Python environment. Download Conda for your OS here: https://www.anaconda.com/download/. Additional information on setting up and managing Conda environments can be found [here](https://conda.io/docs/user-guide/tasks/manage-environments.html). Once you have Conda installed, Follow the instructions below to successfully setup a Python environment on Linux, MacOS, or Windows.

This Python Jupyter Notebook tutorial has been tested using Python version 3.9. 

Using your preferred command line interface (command prompt, terminal, cmder, etc.) type the following to successfully create a compatible python environment:
> `conda create -n gedi -c conda-forge --yes python=3.9 h5py shapely geopandas pandas geoviews holoviews`

Next, activate the Python Environment that you just created.

> `conda activate gedi`

Now you can launch Jupyter Notebook to open the notebooks included.

> `jupyter notebook`

If you do not have Jupyter Notebook installed, you may need to run:

> `conda install jupyter notebook`

**Having trouble getting a compatible Python environment set up? Contact [LP DAAC User Services](https://lpdaac.usgs.gov/lpdaac-contact-us/).**

+ If you do not have an Environment Manager installed, we recommend  [Anaconda](https://www.anaconda.com/products/distribution) or [miniconda](https://docs.conda.io/en/latest/miniconda.html). When installing, be sure to check the box to "Add Anaconda to my PATH environment variable" to enable use of conda directly from your command line interface. If you prefer to not install Conda, the same setup and dependencies can be achieved by using another package manager such as pip.

---

### 2. File Downloads  


Click/copy the URLs into a browser to download the GEDI02_B granule used in this tutorial. Save it next to the notebook in `Apr2023_USFS` folder. You will need a [NASA Earth Data Login](https://urs.earthdata.nasa.gov/profile) to download the data used in this tutorial. You can create an account at the link provided.   
 
+ https://e4ftl01.cr.usgs.gov//GEDI_L1_L2/GEDI/GEDI02_B.002/2022.04.30/GEDI02_B_2022120091720_O19145_02_T09106_02_003_01_V002.h5?_ga=2.154728634.387355792.1681738783-1969705792.1681738783 
---

## Additional GEDI Resources

+ https://github.com/nasa/GEDI-Data-Resources

## Contact Info:  

Email: LPDAAC@usgs.gov  
Voice: +1-866-573-3222  
Organization: Land Processes Distributed Active Archive Center (LP DAAC)¹  
Website: <https://lpdaac.usgs.gov/>  
Date last modified: 04-19-2023  

¹Work performed under USGS contract G15PD00467 for NASA contract NNG14HH33I.  
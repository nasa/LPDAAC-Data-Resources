# Repository Setup Instructions

The tutorials and how-tos in all repositories developed by LP DAAC team require a [NASA Earthdata account](https://urs.earthdata.nasa.gov/), an installation of [Git](https://git-scm.com/downloads), and a compatible Python Environment. See details on prerequisites and Python environment Setup instructions below. 

---

## 1. Prerequisites

+ To access or download NASA Earth data using Python, a [NASA Earthdata account](https://urs.earthdata.nasa.gov/) and a `.netrc` file with your NASA Earthdata Login credentials are required. You can manually create a `.netrc` file, but all notebooks requiring access have an example of signing in using `earthaccess`. The `earthaccess.login(persist=True)` function will prompt for your NASA Earthdata username and password and create a `.netrc` if one does not exist.

+ Install Environment Manager:
  
  + For local Python environment setup we recommend using [mamba](https://mamba.readthedocs.io/en/latest/) to manage Python packages. To install *mamba*, download [miniforge](https://github.com/conda-forge/miniforge) for your operating system. If using Windows, be sure to check the box to "Add mamba to my PATH environment variable" to enable use of mamba directly from your command line interface. **Note that this may cause an issue if you have an existing mamba install through Anaconda.**    

+ If you do not have Git, you can [download](https://git-scm.com/downloads) and install it. 
 
## 2. Python Environment Setup  

The Python environment included in this repository will work for all tutorials developed by LP DAAC team.  All required packages are included in an `.yml` file stored in `setup` folder. Using your preferred command line interface (command prompt, terminal, cmder, etc.) follow the steps below to create a compatible Python environment.

Type the following in the command line and press enter to create a compatible environment with the most updated packages. It should work for both Windows and MacOS.

```
mamba env create -f setup/environment.yml
```  

Alternatively, if you would prefer to have build the environment by listing out packages, the list below can be used.

```
mamba create -n lpdaac -c conda-forge --yes python=3.12 gdal fiona hvplot geoviews rioxarray rasterio jupyter geopandas earthaccess jupyter_bokeh h5py h5netcdf spectral scikit-image jupyterlab seaborn dask ray-default pystac-client odc-stac pyresample libgdal-hdf4 harmony-py
```

Next, activate the environment.

```
mamba activate lpdaac
```

To setup a Python environment to work with resources in the Cloud (AWS `use-west-2` region) follow the [Cloud Environment Setup instruction](https://nasa-openscapes.github.io/earthdata-cloud-cookbook/environment-setup/).

## 3. Opening the notebooks

Navigate to the repository where the Jupyter notebooks or Python scripts you want to run are located. Now you can run your python script or launch Jupyter Notebook by typing the following in command line:

```
jupyter notebook
```

If returning to an already created but inactive environment, using your preferred command line interface (command prompt, terminal, cmder, etc.) navigate to your local copy of the repository, then type the following to activate the Python Environment:

```
mamba activate lpdaac
```

Now you can launch Jupyter Notebook to open the notebooks included.

```
jupyter notebook
```

**Still having trouble getting a compatible Python environment set up? Contact [LP DAAC User Services](https://lpdaac.usgs.gov/lpdaac-contact-us/).**  

## Contact Info  

Email: <LPDAAC@usgs.gov>  
Voice: +1-866-573-3222  
Organization: Land Processes Distributed Active Archive Center (LP DAAC)¹  
Website: <https://lpdaac.usgs.gov/>  

¹Work performed under USGS contract G15PD00467 for NASA contract NNG14HH33I.  



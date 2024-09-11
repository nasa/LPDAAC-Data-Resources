# Accessing NASA LP DAAC Data

This guide summarizes the various ways to find and access NASA data hosted at Land Processes Distributed Active Archive Center (LP DAAC).  

## Web Applications

### NASA Earthdata Search

 [NASA Earthdata Search](https://search.earthdata.nasa.gov/search) is a powerful search and discovery application for NASA's Earth Observing System Data and Information System (EOSDIS). Users can search across a wide range of NASA's Earth science data, filter granules by temporal range and region of interest (ROI), view collection and granule-level metadata, and dowload granules and customized outputs.  

 Interested in bulk downloading of files? Visit the guides available at: <https://github.com/nasa/LPDAAC-Data-Resources/tree/main/guides>  

### AppEEARS  

The [Application for Extracting and Exploring Analysis Ready Samples (AppEEARS)](https://appeears.earthdatacloud.nasa.gov/) offers a streamlined way to access, subset, transform, and visualize geospatial data from NASA's Earthdata Cloud and other federal data archives. AppEEARS provides an intuitive graphical user interface (GUI) and a powerful application programming interface (API), allowing users to extract data from multiple collections and return results in a common projection and analysis-ready file format. By using AppEEARS, users can save time by reducing preprocessing needs, receive results in their selected formats with quality information, and minimize data download requirements. To get started, visit the [Available Products](https://appeears.earthdatacloud.nasa.gov/products) page for a complete list of accessible data, explore the [AppEEARS documantation](https://appeears.earthdatacloud.nasa.gov/help) for a step-by-step guide, and check out the [AppEEARS Data Resources](https://github.com/nasa/AppEEARS-Data-Resources) in GitHub for additional guides, tutorials, and resources.

## Programmatic Access

### CMR API  

[NASA's Common Metadata Repository (CMR)](https://www.earthdata.nasa.gov/eosdis/science-system-description/eosdis-components/cmr) is a metadata system that catalogs all data and service metadata records for NASA's Earth Observing System Data and Information System (EOSDIS) data including data hosted by the LP DAAC. With CMR, users can programmatically discover data using the [CMR API](https://cmr.earthdata.nasa.gov/search/site/docs/search/api.html), which supports REST client requests for metadata information. Furthermore, R and Python packages (see below) are available to simplify data exploration and access, making it easier to find and utilize the data you need.

Visit the tutorials available in [LPDAAC-Data-Resources](https://github.com/nasa/LPDAAC-Data-Resources/tree/main/python/tutorials) to learn more about accessing data directly from CMR API.  

### AppEEARS API

The [AppEEARS API](https://lpdaacsvc.cr.usgs.gov/appeears/api/) is a RESTful API that allows users to access the same functionality as the AppEEARS web application. The API provides users with the ability to subset, reformat, and visualize data from a variety of federal data archives. The API documentation can be found [here](https://lpdaacsvc.cr.usgs.gov/appeears/api/) and provides step by step instructions on how to work with AppEEARS web application and API. Additionally, [AppEEARS Data Resources Gilthub](https://github.com/nasa/AppEEARS-Data-Resources) includes guides and tutorials on how to utilize AppEEARS.  

### `earthaccess` Python Library  

The [`earthaccess`](https://github.com/nsidc/earthaccess) is a Python library that simplifies querying, accessing, and downloading/streaming of NASA Earth science data from Python. Detailed information, how-tos, and tutorials can be found [here](https://earthaccess.readthedocs.io/en/latest/). Check the [EMIT access Python tutorial](https://github.com/nasa/EMIT-Data-Resources/blob/main/python/how-tos/How_to_find_and_access_EMIT_data.ipynb) how to incorporate `earthaccess` in your workflows.  

### `Earthdatalogin` R Package

The [`Earthdatalogin`](https://cran.r-project.org/web/packages/earthdatalogin/) R library provides convenient authentication and access to cloud-hosted NASA Earth science data products. This package is compatible with R packages that are widely used with cloud native earth observation data (such as 'terra', 'sf', etc.). View the [documentation](https://cran.r-project.org/web/packages/earthdatalogin/earthdatalogin.pdf) for more details.  

### CMR STAC API

[NASA's CMR-STAC](https://github.com/nasa/cmr-stac) API is a web API that allows users to search and access NASA's Earth science data collections using the SpatioTemporal Asset Catalog (STAC) specification. The CMR STAC API is built on top of NASA's Common Metadata Repository (CMR), which catalogs metadata records for NASA's Earth Observing System Data and Information System (EOSDIS) data. By using the STAC specification, the CMR STAC API enables users to search and access data from multiple NASA data centers and repositories, including the LP DAAC, in a standardized and interoperable way. Read the [documentation](https://github.com/nasa/cmr-stac/blob/master/docs/usage/usage.md) for more details.  

Visit the [HLS tutorial in R](https://github.com/nasa/HLS-Data-Resources/blob/main/r/HLS_Tutorial.Rmd) to learn how to utilize `Earthdatalogin` and CMR STAC API.  

## Contact Info  

Email: <LPDAAC@usgs.gov>  
Voice: +1-866-573-3222  
Organization: Land Processes Distributed Active Archive Center (LP DAAC)¹  
Website: <https://lpdaac.usgs.gov/>  
Date last modified: 07-11-2023  

¹Work performed under USGS contract G15PD00467 for NASA contract NNG14HH33I.  

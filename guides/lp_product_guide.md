# Land Data Products Guide

## General Tools and Applications

### [LP DAAC Website](https://lpdaac.usgs.gov/)

---

#### Quick Links

- **Data Catalog**: <https://lpdaac.usgs.gov/product_search/?status=Operational>
- **News**: <https://lpdaac.usgs.gov/news/>
- **Help**: <https://lpdaac.usgs.gov/lpdaac-contact-us/>


### NASA [Earthdata Search](https://search.earthdata.nasa.gov/search)

---

**Description**

[Earthdata Search](https://search.earthdata.nasa.gov/search) is NASA's comprehensive data discovery and access platform. Search, visualize, and download Earth science data from NASA's vast archives, covering climate, weather, land, ocean, and more.

**Interface**

- Graphical User Interface (GUI)

**Capabilities**

- Search
- Transformations
- Download

### NASA Earthdata [AppEEARS](https://appeears.earthdatacloud.nasa.gov/)

---

**Description**

[AppEEARS](https://appeears.earthdatacloud.nasa.gov/) simplifies geospatial data access and transformation, allowing users to easily subset datasets from multiple federal archives by point or area locations, time, and layers. The tool provides interactive data previews with quality decoding, and enables users to explore their data before downloading.

**Interface**

- GUI ([Documentation](https://appeears.earthdatacloud.nasa.gov/help))
- Application Programming Interface (API) ([Documentation](https://appeears.earthdatacloud.nasa.gov/api/))

**Capabilities**

- Search
- Processing (point/area extraction, mosaic, clip, reproject, quality decoding, data format )
- Explore
- Download/Access

**Resources**

- [AppEEARS Data Resources](https://github.com/nasa/AppEEARS-Data-Resources)


> **For a more detailed information on how to sccess NASA LP DAAC Data, please refer to the [LP DAAC access data guide](https://github.com/nasa/LPDAAC-Data-Resources/blob/main/guides/NASA_LPDAAC_Data_Access_Guide.md).**

### USGS [EarthExplorer](https://earthexplorer.usgs.gov/)

---

**Description**

EarthExplorer allows users to search, download, and order data held in USGS archives

through many query options
**Interface**

- GUI ([Documentation](https://www.usgs.gov/media/files/earthexplorer-peform-a-search-help-document))
- API ([Machine2Machine API Resources](https://m2m.cr.usgs.gov/))

**Capabilities**

- Search
- Visualization (Footprint)
- Download

View the previous webinar on [exploring EarthExplorer](https://www.youtube.com/watch?v=lkbzQunkT_s&list=PL6df2u6b8WNZnAuUHyC23xLFIYrsgZz6b&index=5) to learn more.


> **NOTE**: NASA LP DAAC data products were removed from USGS’s EarthExplorer and Machine-to-Machine (M2M) API on **August 30, 2024** ([News Announcement](https://lpdaac.usgs.gov/news/nasa-lp-daac-products-removed-from-usgs-earthexplorer-and-machine-to-machine-api-on-august-30-2024/)). Users are encouraged to use NASA’s [Earthdata Search](https://search.earthdata.nasa.gov/search) and/or [AppEEARS](https://appeears.earthdatacloud.nasa.gov/) to discover and download [LP DAAC data products](https://lpdaac.usgs.gov/product_search/?status=Operational). For those who used M2M for programmatic search and access, please explore the [AppEEARS API](https://appeears.earthdatacloud.nasa.gov/api/), the [CMR API](https://cmr.earthdata.nasa.gov/search/site/docs/search/api.html), or the [`earthaccess`](https://earthaccess.readthedocs.io/en/latest/) Python package

## Data Collection Resources

### Harmonized Landsat Sentinel-2 (HLS)

---

### Product Landing Page

- [HLSL30 v2.0](https://doi.org/10.5067/HLS/HLSL30.002)
- [HLSS30 v2.0](https://doi.org/10.5067/HLS/HLSS30.002)

### Resources

#### Graphical User Interfaces / Applications

- [**Earthdata Search**](https://search.earthdata.nasa.gov/search)
- [**AppEEARS**](https://appeears.earthdatacloud.nasa.gov/)

#### Tutorials and Scripts

- [HLS Data Resources](https://github.com/nasa/HLS-Data-Resources) GitHub Repository

### ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS)

---

### Product Landing Pages

- [ECOSTRESS v2.0 Products](https://lpdaac.usgs.gov/product_search/?collections=ECOSTRESS&collection_version_id=2&status=Operational&view=cards&sort=title) - All Available Products
- [ECOSTRESS v1.0 Products](https://lpdaac.usgs.gov/product_search/?collections=ECOSTRESS&collection_version_id=1&status=Operational&view=cards&sort=title)

### Resources

#### Graphical User Interfaces / Applications

- [**Earthdata Search**](https://search.earthdata.nasa.gov/search)
- [**AppEEARS**](https://appeears.earthdatacloud.nasa.gov/)

#### Tutorials and Scripts

- [ECOSTRESS Data Resources](https://github.com/nasa/ECOSTRESS-Data-Resources) GitHub Repository
- [ECOSTRESS Tutorials](https://github.com/ECOSTRESS-Tutorials) managed by NASA JPL
- [VSWIR Imaging and Thermal Applications, Learning, and Science (VITALS)](https://github.com/nasa/VITALS) GitHub Repository


### Global Ecosystem Dynamics Investigation (GEDI)

---

### Product Landing Pages

- [GEDI v2.0 Products](https://lpdaac.usgs.gov/product_search/?collections=GEDI&status=Operational&view=cards&sort=title)

### Resources

#### Graphical User Interfaces / Applications

- [**Earthdata Search**](https://search.earthdata.nasa.gov/search)

#### Tutorials and Scripts

- [GEDI Data Resources](https://github.com/nasa/GEDI-Data-Resources) GitHub Repository

### Earth Surface Mineral Dust Source Investigation (EMIT)

---

### Product Landing Pages

- [EMIT v1.0 Products](https://lpdaac.usgs.gov/product_search/?collections=EMIT&status=Operational&view=cards&sort=title) - All Available Products
- [EMIT L2A Estimated Surface Reflectance (EMITL2ARFL.001)](https://doi.org/10.5067/EMIT/EMITL2ARFL.001)

### Resources

#### Graphical User Interfaces / Applications

- [**Earthdata Search**](https://search.earthdata.nasa.gov/search)
- [**AppEEARS**](https://appeears.earthdatacloud.nasa.gov/)

#### Tutorials and Scripts

- [EMIT Data Resources](https://github.com/nasa/EMIT-Data-Resources) GitHub Repository
- [VSWIR Imaging and Thermal Applications, Learning, and Science (VITALS)](https://github.com/nasa/VITALS) GitHub Repository

### Landsat

---

### Product Landing Pages

- [Landsat Collection 2 Information](https://www.usgs.gov/landsat-missions/landsat-collection-2)

### Resources

#### Graphical User Interfaces / Applications

- [**EarthExplorer**](https://earthexplorer.usgs.gov/)
- [**AppEEARS**](https://appeears.earthdatacloud.nasa.gov/) - Has access to [Landsat Collection 2 U.S. Analysis Ready Data](https://www.usgs.gov/landsat-missions/landsat-collection-2-us-analysis-ready-data)

#### Tutorials and Scripts

- <https://code.usgs.gov/eros-user-services/>

## Additional Resources

### `earthaccess` - Python package for simplifying authentication and querying NASA data collections and assets

- [`earthaccess` GitHub Repository](https://github.com/nsidc/earthaccess/)
- [`earthaccess` Documentation](https://earthaccess.readthedocs.io/en/latest/)
- [`earthaccess` tutorial](https://github.com/CU-ESIIL/HYR-SENSE/blob/main/notebooks/how_to/earthaccess_Introduction.ipynb)

### LP DAAC Managed Repositories

- [LP DAAC Data Use Resources](https://github.com/nasa/LPDAAC-Data-Resources)

## Contact Info  

Email: <LPDAAC@usgs.gov>  
Voice: +1-866-573-3222  
Organization: Land Processes Distributed Active Archive Center (LP DAAC)¹  
Website: <https://lpdaac.usgs.gov/>  
Date last modified: 09-23-2024  

¹Work performed under USGS contract 140G0121D0001 for NASA contract NNG14HH33I.

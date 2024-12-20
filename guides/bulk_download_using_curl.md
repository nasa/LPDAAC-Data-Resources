# How to bulk download LP DAAC data using Curl  

This guide shows how to bulk download [LP DAAC](https://lpdaac.usgs.gov/) data using [cURL](https://curl.se/) from the command line. **cURL** is a free and open source software developed under Client for URLs (cURL) project as a command line tool for transfering data using URLs.

## Requirements:
- [Install cURL](https://curl.se/download.html). View [installing curl instructions](https://developer.zendesk.com/documentation/api-basics/getting-started/installing-and-using-curl/#installing-curl) for more details.

- NASA Earthdata login credentials are required to access data from all NASA DAACs. You can create an account [here](https://urs.earthdata.nasa.gov/users/new).

## Step 1: Save the Download Link(s)  
Save download links for your data as a text file using [Nasa Earthdata Search](https://search.earthdata.nasa.gov/search) or [Common Metadata Repository (CMR)](https://www.earthdata.nasa.gov/eosdis/science-system-description/eosdis-components/cmr) API. Follow the steps in the [Earthdata Search guide](https://github.com/nasa/EMIT-Data-Resources/blob/main/guides/Getting_EMIT_Data_using_EarthData_Search.md) to find your data and save the download links. If you prefer to use an API to find your data and save the download links, a tutorial on how to use the CMR API can be found [here](https://github.com/nasa/LPDAAC-Data-Resources/blob/main/python/tutorials/Data_Discovery_CMR_API_Request.ipynb). 

## Step 2: Set up a .netrc file for Authentication
Follow the instruction on how to create a `.netrc` file [here](https://github.com/nasa/LPDAAC-Data-Resources/tree/bulk_query/guides/create_netrc_file.md) to set up the file using your Earthdata Login Credentials. 

## Step 3: Download LP DAAC Data
You should now be able to run the command to download data directly from the LP DAAC. 
- Navigate to the directory you want to save the data using `cd Insert_Your_Directory`.
- To download a single file, replace the `Insert_the_Download_Link`  in the command below with the URL to the data file you wish to download.
  ```
  curl -O -b ~/.urs_cookies -c ~/.urs_cookies -L -n Insert_the_Download_Link
  ``` 
  Example:
  ```tet
  curl -O -b ~/.urs_cookies -c ~/.urs_cookies -L -n https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/HLSS30.020/HLS.S30.T12SWF.2023189T175919.v2.0/HLS.S30.T12SWF.2023189T175919.v2.0.B08.tif 
  ``` 
- To download multiple files, replace `Insert_Text_File` in the command below with the full path to the text file saved previously in Step 1. 
  ```
  xargs -n 1 curl -O -b ~/.urs_cookies -c ~/.urs_cookies -L -n < Insert_Text_File
  ``` 

  Example:
  ```
   xargs -n 1 curl -O -b ~/.urs_cookies -c ~/.urs_cookies -L -n < data/Granule-DownloadLinks.txt
  ```

# Useful Links:
- https://wiki.earthdata.nasa.gov/display/EL/How+To+Access+Data+With+cURL+And+Wget 

## Contact Info:  

Email: LPDAAC@usgs.gov  
Voice: +1-866-573-3222  
Organization: Land Processes Distributed Active Archive Center (LP DAAC)¹  
Website: <https://lpdaac.usgs.gov/>  
Date last modified: 07-11-2023  

¹Work performed under USGS contract G15PD00467 for NASA contract NNG14HH33I.  


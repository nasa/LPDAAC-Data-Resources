# How to bulk download LP DAAC data using Curl  

This guide shows how to bulk download [LP DAAC](https://lpdaac.usgs.gov/) data using [cURL](https://curl.se/) from the command line. **cURL** is free and open source software developed under Client for URLs (cURL) project. curl is a command line tool for transfering  data using URL.
---

## Requirements:
- You need to [install the latest version of cURL](https://curl.se/download.html). View [installing curl instruction](https://developer.zendesk.com/documentation/api-basics/getting-started/installing-and-using-curl/#installing-curl) for more details.

- NASA Earthdata login credentials are required to access data from LP DAAC. You can create an account [here](https://urs.earthdata.nasa.gov/users/new).
---

## Step 1: Save the Download Link(s)  
Save download links of your data as a text file using [Nasa Earthdata Search](https://search.earthdata.nasa.gov/search) or [Common Metadata Repository (CMR)](https://www.earthdata.nasa.gov/eosdis/science-system-description/eosdis-components/cmr) API. Follow the steps in [Earthdata Search guide](https://github.com/nasa/EMIT-Data-Resources/blob/main/guides/Getting_EMIT_Data_using_EarthData_Search.md) to find your data and save the download links. If you prefer to use API to find your data and save the download links tutorial on how to use CMR API can be found [here](https://github.com/nasa/LPDAAC-Data-Resources/blob/main/python/tutorials/Data_Discovery_CMR_API_Request.ipynb). 
---

## Step 2: Set up a .netrc file for Authentication
Set up a .netrc file in your home directory.


- ### Manual set up:
  - Downlaod [.netrc template file](https://github.com/nasa/LPDAAC-Data-Resources/tree/main/data/.netrc) and save it in your home directory.
    - Insert your NASA Earthdata login username (<USERNAME>)
    - Insert your NASA Earthdata login password (<PASSWORD>)

- ### Command Line:
  - Enter the following in Terminal:
    - #### windows
      To Create a .netrc file, enter the following in the command line. 
      ```
      NUL >> %userprofile%\.netrc | echo machine urs.earthdata.nasa.gov >> %userprofile%\.netrc
      ```
      To insert your NASA Earthdata login username and password into the file, enter the following in the Command Prompt and replace your username and password.

      ```
      echo login Insert_Your_Username >> %userprofile%\.netrc | echo password Insert_Your_Password >> %userprofile%\.netrc
      ```
    - #### MacOS:

      To Create a .netrc file, enter the following in the command line. 
      ```
      touch ~/.netrc | chmod og-rw ~/.netrc | echo machine urs.earthdata.nasa.gov >> ~/.netrc
      ```
      To insert your NASA Earthdata login username and password into the file, enter the following in the Command Prompt and replace your username and password.

      ```
      echo login Inser_Your_Username >> ~/.netrc | echo password Insert_Your_Password >> ~/.netrc
      ```

- ### Programmatically:
  - Run [Authentication for NASA Earthdata notebook](https://github.com/nasa/LPDAAC-Data-Resources/blob/main/python/how-tos/Earthdata_Authentication__Create_netrc_file.ipynb) to create _.nerc_ file. 
  - Alternatively, you can run the [EarthdataLoginSetup script](https://github.com/nasa/LPDAAC-Data-Resources/blob/main/python/scripts/EarthdataLoginSetup.py) in an interpreter or in the command line.
---

## Step 3: Download LP DAAC Data
You should now be able to run the command to download data directly from the LP DAAC. 
- Navigate to the directory you want to save the data using `cd Insert_Your_Directory`.
- To download a single file, replace the download link and enter the line below in the command line.
  ```
  curl -O -b ~/.urs_cookies -c ~/.urs_cookies -L -n Insert_the_Download_link
  ``` 
  Example:
  ```tet
  curl -O -b ~/.urs_cookies -c ~/.urs_cookies -L -n https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/HLSS30.020/HLS.S30.T12SWF.2023189T175919.v2.0/HLS.S30.T12SWF.2023189T175919.v2.0.B08.tif 
  ``` 
- To download multiple files, use the full path of text file saved previously in step 1 below. 
  ```
  xargs -n 1 curl -O -b ~/.urs_cookies -c ~/.urs_cookies -L -n < Insert_the_Full_Path
  ``` 

  Example:
  ```
   xargs -n 1 curl -O -b ~/.urs_cookies -c ~/.urs_cookies -L -n < data/Granule-DownloadLinks.txt
  ```

------------------
# Useful Links:
- https://wiki.earthdata.nasa.gov/display/EL/How+To+Access+Data+With+cURL+And+Wget 
---

## Contact Info:  

Email: LPDAAC@usgs.gov  
Voice: +1-866-573-3222  
Organization: Land Processes Distributed Active Archive Center (LP DAAC)¹  
Website: <https://lpdaac.usgs.gov/>  
Date last modified: 07-11-2023  

¹Work performed under USGS contract G15PD00467 for NASA contract NNG14HH33I.  


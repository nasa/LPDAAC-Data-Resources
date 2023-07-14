# How to bulk download LP DAAC data using wget  

This guide shows how to bulk download [LP DAAC](https://lpdaac.usgs.gov/) data using [wget](https://www.gnu.org/software/wget/) from the command line. The wget command is a tool developed by the GNU Project to download files from the web. Wget allows you to automate retrieving content and files from web servers using a command-line interface. 
---

## Requirements:
- [Install wget](https://ftp.gnu.org/gnu/wget/). View [Frequently Asked Questions About Downloading GNU Wget](http://wget.addictivecode.org/FrequentlyAskedQuestions.html#download) for more details.
- NASA Earthdata Login credentials are required to access data from all NASA DAACs. You can create an account [here](https://urs.earthdata.nasa.gov/users/new).
---

# Method 1: Authenticate using .wgetrc file
## Step 1: Save the Download Link(s)  

Save download links for your data as a text file using [Nasa Earthdata Search](https://search.earthdata.nasa.gov/search) or [Common Metadata Repository (CMR)](https://www.earthdata.nasa.gov/eosdis/science-system-description/eosdis-components/cmr) API. Follow the steps in the [Earthdata Search guide](https://github.com/nasa/EMIT-Data-Resources/blob/main/guides/Getting_EMIT_Data_using_EarthData_Search.md) to find your data and save the download links. If you prefer to use an API to find your data and save the download links, a tutorial on how to use the CMR API can be found [here](https://github.com/nasa/LPDAAC-Data-Resources/blob/main/python/tutorials/Data_Discovery_CMR_API_Request.ipynb). 


## Step 2: Set up a .wgetrc file for Authentication

Set up a .wgetrc file in your home directory.

- ### Manual setup:
  - Download the [.wgetrc template file](https://github.com/nasa/LPDAAC-Data-Resources/tree/main/data/.wgetrc) and save it in your home directory.
    - Open the .wgetrc file in a text editor and replace `<USERNAME>` with your NASA Earthdata Login username and `<PASSWORD>` with your NASA Earthdata Login password.
    


- ### Command Line:
  - To Create a .wgetrc file, enter the following in Terminal.
    - #### windows
      ```text
      NUL >> .wgetrc
      ```
    - #### MacOS, Linux, Cmder:

      To Create a .netrc file, enter the following in the command line. 
      ```text
      touch .wgetrc | chmod og-rw .wgetrc
      ```
  - To insert your NASA Earthdata login username and password into the file, enter the following in the Command Prompt and replace your username and password.

      ```text
      echo http-user=Insert_Your_Username >> .wgetrc | echo http-password=Insert_Your_Password >> .wgetrc
      ```

## Step 3: Download LP DAAC Data

You should now be able to run wget commands to download data directly from the LP DAAC. 
- Navigate to the directory you want to save the data using `cd Insert_Your_Directory`.
- To download a single file, replace the download link and enter the line below in the command line.
  ```text
  wget Insert_the_Download_link
  ``` 
  Example:
  ```text
  wget https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/HLSS30.020/HLS.S30.T12SWF.2023189T175919.v2.0/HLS.S30.T12SWF.2023189T175919.v2.0.B08.tif 
  ``` 
- To download multiple files, use the full path of text file saved previously in step 1 below. 
  ```text
  wget -i Insert_Text_File
  ``` 
  Example:
  ```text
  wget -i data/Granule-DownloadLinks.txt

  ```

---
# Method 2: Authenticate Manually

If you prefer to not create .wget for authentication, you can make wget command to work by passing authentications manually.

## Step 1: Save the Download Link(s)  

Save download links of your data as a text file using [Nasa Earthdata Search](https://search.earthdata.nasa.gov/search) or [Common Metadata Repository (CMR)](https://www.earthdata.nasa.gov/eosdis/science-system-description/eosdis-components/cmr) API. Follow the steps in [Earthdata Search guide](https://github.com/nasa/EMIT-Data-Resources/blob/main/guides/Getting_EMIT_Data_using_EarthData_Search.md) to find your data and save the download links. If you prefer to use API to find your data and save the download links tutorial on how to use CMR API can be found [here](https://github.com/nasa/LPDAAC-Data-Resources/blob/main/python/tutorials/Data_Discovery_CMR_API_Request.ipynb). 


## Step 2: Download LP DAAC Data

To run wget commands to download data directly from the LP DAAC. 

- Navigate to the directory you want to save the data using `cd Insert_Your_Directory`.
- Replace your Earthdata login username with "Insert_Your_Username" below.
  - To download a single file, replace the `Insert_the_Download_Link`  in the command below with the URL to the data file you wish to download
    ```
    wget --http-user=Insert_Your_Username --ask-password --keep-session-cookies Insert_the_Download_Link
    ```
     Example:
    ```
    wget --http-user=MYUSERNAME --ask-password --keep-session-cookies https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/HLSS30.020/HLS.S30.T12SWF.2023189T175919.v2.0/HLS.S30.T12SWF.2023189T175919.v2.0.B08.tif
    ```
  
  - To download multiple files, replace `Insert_Your_Username` with your Earthdata Login username in the command below. Also, replace `Insert_Text_File` with the full path to the text file saved previously in Step 1. You will be asked to enter your `password` (i.e., you Earthdata Login password) after running the command. You'll press enter again to download your files.  
  
    ```
    wget --http-user=Insert_Your_Username --ask-password --keep-session-cookies -i Insert_Text_File
    ```

    Example:
    ```
    wget --http-user=MYUSERNAME --ask-password --keep-session-cookies -i data/Granule-DownloadLinks.txt
    ```
  **Alternatively, you can replace `--ask-password` with `--http-passwd=Insert_Your_Password` and enter your password directly in the command line.** 

---

## Contact Info:  

Email: LPDAAC@usgs.gov  
Voice: +1-866-573-3222  
Organization: Land Processes Distributed Active Archive Center (LP DAAC)¹  
Website: <https://lpdaac.usgs.gov/>  
Date last modified: 07-12-2023  

¹Work performed under USGS contract G15PD00467 for NASA contract NNG14HH33I.  

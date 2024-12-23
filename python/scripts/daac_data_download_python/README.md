# How to Access the LP DAAC From Data Pool and NASA Earthdata Cloud
---
# Objective:
The `DAACDataDownload.py` script demonstrates how to configure a connection to download data directly in Python from an Earthdata Login-enabled server, specifically the [LP DAAC Data Pool](https://www.earthdata.nasa.gov/learn/use-data/tools) and [NASA Earthdata Cloud](https://www.earthdata.nasa.gov/). The script is a command line executable, where a user will submit either a single URL to a file to be downloaded, or the location of a csv or text file containing multiple URLs to be downloaded, and a desired directory to download files to. 


The script begins with authenticating and then downloads the URL(s) that you provided. If multiple URLs are included in the file list, the script loops through URLs and downloads 8 files at a time using the `earthaccess` multithreading download method to speed up the download process. If the files provided in your list exist in the provided directory, the script skips those files. The output file name will be the same as the input file name.   

---
## Prerequisites/Setup Instructions  

### Environment Setup 

If you do not have an Environment Manager installed, we recommend [mamba](https://mamba.readthedocs.io/en/latest/) to manage Python packages. Details instruction on how to install an environment manager can be found [here](https://github.com/nasa/LPDAAC-Data-Resources/blob/main/setup/setup_instructions_python.md). Once you have it installed, type the following in your preferred command line interface (command prompt, terminal, cmder, etc.) to create a compatible environment.

```
mamba create -n daac-download -c conda-forge earthaccess
```
**If you are using conda, replace the "mamba" with "conda" and be patient.**

Instruction for setting up a compatible environment for all LP DAAC Python resources is available at: <https://github.com/nasa/LPDAAC-Data-Resources/blob/main/setup/setup_instructions_python.md>

### NASA Earthdata Login:

**You will need a NASA Earthdata Login account to download LP DAAC data (and use this script).** To create a NASA Earthdata Login account, go to the [Earthdata Login website](https://urs.earthdata.nasa.gov) and click the “Register” button, which is next to the green “Log In” button under the Password entry box. Fill in the required boxes (indicated with a red asterisk), then click on the “Register for Earthdata Login” green button at the bottom of the page. An email including instructions for activating your profile will be sent to you. Activate your profile to complete the registration process.

To download data from the LP DAAC archive, you need to authorize our applications to view your NASA Earthdata Login profile. Once authorization is complete, you may resume your session.
To authorize Data Pool, please [click here](https://urs.earthdata.nasa.gov/approve_app?client_id=ijpRZvb9qeKCK5ctsn75Tg&_ga=2.128429068.1284688367.1541426539-1515316899.1516123516).  

### **Netrc file**
The netrc file is needed to download NASA Earthdata science data from a scripting environment like Python. There are multiple methods to [create a .netrc file for authntication](https://github.com/nasa/LPDAAC-Data-Resources/tree/main/guides/create_netrc_file.md). Here, the `earthaccess` package is used to automatically create a `.netrc` file using your Earthdata login credentials. If one does not exist, you will be prompted to enter your Earthdata Login credentials.
---

# Procedures:

## Getting Started:

> #### 1. Save a download URL for your data from  [NASA Earthdata Search](https://search.earthdata.nasa.gov/) for a single file. For multiple files, download the text file containing URLs to files.   

> #### 2. Access `DAACDataDownload.py` from [LPDAAC-Data-Resources] Github Repository   
  > 1. You can download the raw file for the script from <https://github.com/nasa/LPDAAC-Data-Resources/blob/main/python/scripts/daac_data_download_python/DAACDataDownload.py> 
   
  > 2. Additionally, you can download all contents of this repository as a [zip file](https://github.com/nasa/LPDAAC-Data-Resources/archive/refs/heads/main.zip). You can also clone the repository by typing `git clone https://github.com/nasa/LPDAAC-Data-Resources.git` in a command line. Navigate to `python/scripts/daac_data_download_python/DAACDataDownload.py`.  

## Script Execution

> #### 1. Activate your MacOS/Windows environment, run the script with the following in your Command Prompt/terminal window:

  > 1.  `python DAACDataDownload.py -dir <insert local directory to save files to> -f <insert a single granule URL, or the location of a csv or text file containing granule URLs>`  
  > - Ex:   `python C:\User\Downloads\DAACDataDownload.py  -dir C:\User\downloads -f C:\User\downloads\ECOSTRESS-granule-list.txt` 
  > - Ex: `python C:\User\Downloads\DAACDataDownload.py  -dir C:\User\downloads -f https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ECO_L2T_LSTE.002/ECOv002_L2T_LSTE_34912_026_54GXQ_20240902T022621_0712_01/ECOv002_L2T_LSTE_34912_026_54GXQ_20240902T022621_0712_01_LST.tif`

  > 2. If you do not have a netrc file configured in your home directory, the script will prompt you for input on your NASA Earthdata Login Username and Password. Enter your username and password and hit enter to continue downloading your data. **Please note that your Earthdata Login info, your username, and password, will be stored in a .netrc file located in the Home directory on this system you are using.** You will get the same message when you run the script as a reminder. If you do not trust the machine you are using, make sure to delete the created netrc file.   
  > 4. Your file(s) will be downloaded at the designated `-dir` assigned above.
---  

## Contact Info  

Email: LPDAAC@usgs.gov  
Voice: +1-866-573-3222  
Organization: Land Processes Distributed Active Archive Center (LP DAAC)¹  
Website: <https://lpdaac.usgs.gov/>  
Date last modified: 12-23-2024  

¹Work performed under USGS contract G15PD00467 for NASA contract NNG14HH33I.  

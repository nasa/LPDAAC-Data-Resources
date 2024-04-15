# R resources Setup Instructions

The R tutorials and how-tos in all repositories developed by LP DAAC team require R and RStudio, compatible R environment with packages used in the scripts, and installation of [Git](https://git-scm.com/downloads). More details can be found below.  

## 1. Prerequisites

+ To access or download NASA Earth data, a `.netrc` file with your NASA Earthdata Login information is needed. You can created an account [here](https://urs.earthdata.nasa.gov/users/new) if you do not have one.

  + Setting up a netrc file:

  + R tutorials leverages a netrc file storing your Earthdata
        login credentials for authentication. This file is assumed to be
        stored in the user profile directory on Window OS or in the home
        directory on Mac OS. Run `source(.../R/modules/earthdata_netrc_setup.R)`
        to ensure you have the proper netrc file set up. If you are prompted
        for your NASA Earthdata Login Username and Password, hit enter once you
        have submitted your credentials. If neither HOME nor Userprofile are
        recognized by R, the current working directory is used.
  + If you want to manually create your own netrc file, download the .netrc
        file template (saved in `Data` folder), add your credentials, and save to your Userprofile/HOME
        directory. You should also make sure that both HOME
        directory and Userprofile directories are as same as a directory
        you are saving the .netrc. To do that run `Sys.setenv("HOME" = "YOUR DIRECTORY")`
        and `Sys.setenv("userprofile" = "YOUR DIRECTORY")`.

+ R and RStudio are required to execute this tutorial. Installation details can be found [here](https://www.rstudio.com/products/rstudio/download/#download).

  + Windows

    + Install and load installr:

      + `install.packages("installr");library(installr)`\

    + Copy/Update the existing packages to the new R installation:

      + `updateR()`

    + Open RStudio, go to Help \> Check for Updates to install newer
            version of RStudio (if available).

  + Mac

    + Go to <https://cloud.r-project.org/bin/macosx/>.\
    + Download the latest release (R-4.0.1.pkg) and finish the
            installation.
    + Open RStudio, go to Help \> Check for Updates to install newer
            version of RStudio (if available).
    + To update packages, go to Tools \> Check for Package Updates. If
            updates are available, select All, and click Install Updates.

+ Check the version of R by typing `version` into the console and RStudio by typing `RStudio.Version()` into the console and update them if needed.
  + The R tutorials have been tested on Windows using R Version 4.2.2 and RStudio version 2022.12.0.353.

------------

## 2. Procedures  

+ [Clone](https://git.earthdata.nasa.gov/scm/lpdur/hls_tutorial_r.git) or [download](https://git.earthdata.nasa.gov/rest/api/latest/projects/LPDUR/repos/hls_tutorial_r/archive?format=zip) HLS_Tutorial_R Repository from the LP DAAC Data User Resources Repository.  

+ When you open this Rmarkdown notebook in RStudio, you can click the little green "Play" button in each grey code chunk to execute the code. The result can be printed either in the R Console or inline in the RMarkdown notebook, depending on your RStudio preferences.

------------------------------------------------------------------------

## 3. R Environment Setup

+ **Required packages:**
  + `getPass`  
  + `sys`  
  + `httr`
  + `raster`
  + `readr`
  + `tidyr`
  + `dplyr`
  + `jsonlite`
  + `geojsonlint`  
  + `geojsonio`  
  + `geojsonR`  
  + `rgdal`
  + `sp`
  + `terra`
  + `warnings`
+ To read and visualize the GeoTIFF:
  + `raster`
  + `rasterVis`
  + `RColorBrewer`
  + `ggplot2`
  
Run the code below in a cell to identify any missing packages to install, and then load
all of the required packages.
Alternatively, you can use `install.packages('package name')` command in the console or use `install.packages(c('package #1', 'package #2',...))` to download multiple packages.

```{}
packages <- c('terra','getPass','httr','jsonlite','ggplot2','dplyr','tidyr','readr','geojsonio','geojsonR','rgdal',
             'sp', 'raster', 'rasterVis', 'RColorBrewer', 'jsonlite', 'geojsonlint', 'magrittr', 'xml2', 
             'dygraphs', 'xts','lubridate','DT','rmarkdown', 'rprojroot','imager')

# Identify missing (not installed) packages
new.packages <- packages[!(packages %in% installed.packages()[,"Package"])]

# Loop through and Install new (not installed) packages
if (length(new.packages)[1]==0){
  message('All packages already installed')
}else{
  for (i in 1:length(new.packages)){
    message(paste0('Installing: ', new.packages))
    install.packages(new.packages[i], repos='http://cran.rstudio.com/')
  }
}
```  

The code below is also saved in `AppEEARS_API_Install.R`

## Contact Info  

Email: <LPDAAC@usgs.gov>  
Voice: +1-866-573-3222  
Organization: Land Processes Distributed Active Archive Center (LP DAAC)¹  
Website: <https://lpdaac.usgs.gov/>  
Date last modified: 09-07-2023  

¹Work performed under USGS contract G15PD00467 for NASA contract NNG14HH33I.  

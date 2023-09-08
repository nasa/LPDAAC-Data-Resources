# Packages you will need for AppEEARS API Tutorials
packages <- c('terra','getPass','httr','jsonlite','ggplot2','dplyr','tidyr','readr','geojsonio','geojsonR','rgdal',
             'sp', 'raster', 'rasterVis', 'RColorBrewer', 'jsonlite', 'geojsonlint', 'magrittr', 'xml2', 
             'dygraphs', 'xts','lubridate','DT','rmarkdown', 'rprojroot','imager')


# Identify missing packages
new.packages <- packages[!(packages %in% installed.packages()[,"Package"])]

# Loop through and download the required packages
if (length(new.packages)[1]==0){
  message('All packages already installed')
}else{
  for (i in 1:length(new.packages)){
    message(paste0('Installing: ', new.packages))
    install.packages(new.packages[i])
  }
}
"""
---------------------------------------------------------------------------------------------------
 How to Access the LP DAAC Data with Python
 The following Python code example demonstrates how to configure a connection to download LP DAAC data 
 from Data Pool or NASA Earthdata Cloud. 
 'earthaccess' package handles the NASA EarthData Login (EDL). 
 Last Updated: 09/06/2024
---------------------------------------------------------------------------------------------------
"""
# Load necessary packages into Python
from subprocess import Popen
from colorama import Fore, Back, Style
import earthaccess 
import argparse
import os

# ----------------------------------USER-DEFINED VARIABLES--------------------------------------- #
# Set up command line arguments
parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-dir', '--directory', required=True, help='Specify directory to save files to')
parser.add_argument('-f', '--files', required=True, help='A single granule URL, or the location of csv or textfile containing granule URLs')
args = parser.parse_args()

saveDir = args.directory  # Set local directory to download to
files = args.files        # Define file(s) to download from the LP DAAC Data Pool

# ---------------------------------SET UP WORKSPACE---------------------------------------------- #
# Create a list of files to download based on input type of files above
if files.endswith('.txt') or files.endswith('.csv'):
    with open(files, 'r') as f:
        fileList = f.read().splitlines() # If input is text/csv file with file URLs
    
    # fileList = open(files, 'r').readlines().splitlines()  
elif isinstance(files, str):
    fileList = [files]                       # If input is a single file
# Check if the directory exists
if not os.path.isdir(saveDir): 
    os.makedirs(saveDir)

# --------------------------------AUTHENTICATION CONFIGURATION----------------------------------- #
# AUthenticate using earthaccess.login function. 

earthaccess.login(strategy = 'netrc', persist = True) 

print(Fore.RED + Back.GREEN + 'Please note: if you just entered your Earthdata Login info, your username and password are now stored in a .netrc file located at the Home directory on this system.')
print(Style.RESET_ALL)
# -----------------------------------------DOWNLOAD FILE(S)-------------------------------------- #
# Loop through and download all files to the directory 8 files at a time, and keeping same filenames
num = int(len(fileList)/8)

for n in list(range(num+1)):
    try:
        subList = fileList[8*(n):8*(n+1)]
    except: 
        try: 
            subList = fileList[8*(n):len(fileList)]
        except: 
            subList = fileList[8*(n)]
    # Remove the files that are downloaded already
    subList_filter = []
    for f in subList:
        if not os.path.isfile(os.path.join(saveDir, f.rsplit('/')[-1])):
            subList_filter.append(f)
        else:
            print(f'{f.rsplit("/")[-1]} already exists in the {saveDir}.')

    if len(subList_filter) != 0:        
        attempts = 0
        success = False
        while (attempts < 3 and success == False):
            try:
                # Download files 
                earthaccess.download(subList_filter, saveDir, threads=8)
                success = True
            except:
                attempts +=1
                print(Fore.RED + Back.GREEN + f'There is an issue with downloading files in {subList_filter}')
                print(Style.RESET_ALL)

   

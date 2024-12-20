# How to Set up a `.netrc` file for Authentication
There are several ways to set up a `.netrc` file in your home directory.

- ### Manual set up
  - Download the [.netrc template file](https://github.com/nasa/LPDAAC-Data-Resources/tree/main/data/.netrc) and save it in your home directory.
    - Open the .netrc file in a text editor and replace `<USERNAME>` with your NASA Earthdata Login username and `<PASSWORD>` with your NASA Earthdata Login password.

- ### Create .netrc file from the Command Line
  - Enter the following in Terminal:
    - #### Windows
      To Create a `.netrc` file, enter the following in the command line. 
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
      echo login Insert_Your_Username >> ~/.netrc | echo password Insert_Your_Password >> ~/.netrc
      ```

- ### Programmatically:
    - #### Python
        The [`earthaccess` Python library](https://earthaccess.readthedocs.io/en/latest/) provides a convenient way to authenticate, search, and access NASA Earth science data using Python. It can be used to manage Earthdata Login and generate access tokens.
        Run the code below to create a `.netrc` file in your home directory. You will be prompted to enter your Earthdata Login credentials.
        ```python
        import earthaccess
        earthaccess.login(persist=True)
        ``` 
        Instruction on how to install the `earthaccess` library is provided [here](https://earthaccess.readthedocs.io/en/latest/quick-start/).

    - #### R 
        The [`earthdatalogin` R Package](https://cran.r-project.org/web/packages/earthdatalogin/index.html) provides convenient authentication and access to NASA 'EarthData' products using R. `edl_netrc` function will create a `.netrc` file using your Earthdata Login (EDL) credentials. 
        ```r
        library(earthdatalogin)
        edl_netrc(username = Insert_Your_Username, password = Insert_Your_Password, netrc_path = '~/.netrc')
        ```
        More details can be found [here](https://github.com/boettiger-lab/earthdatalogin/blob/main/R/edl_netrc.R).


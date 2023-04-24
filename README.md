# NodeV (NVM windows)

## Introduction
This is a script to make it easier to switch between different node version with nvm windows.

1. Open a terminal as administrator
2. Run the python script
`python nodev.py`
3. Select the node version you want to switch to and press enter

## Additional automation
To be able to run the script from anywhere you can create a .bat file at any location included in the path environment variable, for examble C:\Windows. Give the .bat file the same name you want your command to be called, for example nodev.bat
In the bat file add the following:
```
@echo off
python <path-to-python-script>
```
**Make sure to replce `<path-to-python-script>` with the path to the nodev.py file in this project**

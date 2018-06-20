# EDF-to-ASC---EYELINK-DATA-CONVERTER
EyeLink Data File converter. Same process than edf2asc.exe (called in the function).

This function is able to call the edf2asc.exe within a python script to avoid the drag and drop solution to convert eyelink data file to ascii.

Function is able to go through a folder, scan all files within, check if an edf file is present, and convert edf file to asc.

If ascfile does not already exist in the folder, the function is executed, if not it stops.

You can check if the script worked if an ascfile has been created in the same folder of the edf file.

## Actual version
WARNING 1: Don't forget to define your path to get edf2asc.exe

WARNING 2: Don't forget to define before (in your main script) the folder in which you want to convert your edf file.

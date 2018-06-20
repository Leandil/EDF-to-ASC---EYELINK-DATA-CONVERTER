# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 11:50:35 2018
EyeLink Data File converter. Same process than edf2asc.exe (called in the function).
Function able to call the edf2asc.exe within a python script to avoid the drag and drop solution to convert eyelink data file to ascii.
Function is able to go through a folder, scan all files within, check if an edf file is present, and convert edf file to asc.
If ascfile does not already exist in the folder, the function is executed, if not it stops.
You can check if the script worked if an ascfile has been created in the same folder of the edf file.

WARNING 1: Don't forget to define your path to get edf2asc.exe
WARNING 2: Don't forget to define before (in your main script) the folder in which you want to convert your edf file. 
@author: A.P
"""
import os ; import subprocess ; 
def checkasc(m,n):     
        cmd = path + "\edf2asc.exe" ## path and call of edf2asc.exe 
        os.chdir(pathfolder+filename ) ## folder + file path - type str
        dir1 = os.path.dirname(pathfolder+filename) ## file path - type str
        for root,dirs,files in os.walk(dir1):
           for file in sorted(files):
               if file.endswith(".edf"): ## check if edf file exists in the folder 
                       ascfile = file[:-3]+"asc" ## create ascfile name from the edf name
                       if not os.path.isfile(ascfile) : ## check if an ascfile with this name already exists
                           subprocess.run([cmd, file]) ## if not, execute and convert edftoasc
#                           subprocess.Popen([cmd,file])

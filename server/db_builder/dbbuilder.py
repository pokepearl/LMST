#!/usr/bin/env python3
import sqlite3
import os
import formic # This is a special Python 3 compatible version of Formic
# Checking root folder, this should be rewritten
dircheck = input('Is this script being run from the root directory of the LMST webserver? (yes/no): ')
if dircheck == "yes":
    print('Continuing...')
elif dircheck == "no":
    print('Exiting, rerun from the webserver root')
    raise SystemExit(1)
else:
    print('Invalid response, Exiting')
    raise SystemExit(1)
# Glob all files with approved extensions
currentdir = os.getcwd()+'/Music/' #Default Music Directory
muspattern = ["*.mp3", "*.ogg", "*.opus"] # Default Extensions
filelist = formic.FileSet(directory=currentdir, include=muspattern)
musiclist = [] #Predefine Music List
for filename in filelist.qualified_files():
    musiclist.append(filename)
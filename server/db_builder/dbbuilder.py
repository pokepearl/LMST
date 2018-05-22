#!/usr/bin/env python3
import sqlite3
import os
import formic # This is a special Python 3 compatible version of Formic
import mutagen
import subprocess
import re
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
    # Append Music File to List
    musiclist.append(filename)
# Configure SQLite
connect = sqlite3.connect('lmst.db')
cursor = connect.cursor()
cursor.execute('DROP TABLE IF EXISTS songs')
cursor.execute('CREATE TABLE songs (title text,artist text,album text,length text)')
for fname in musiclist:  # Start Scraping info from songs and append to DB
    parsefile = subprocess.Popen(["mutagen-inspect", fname], stdout=subprocess.PIPE) # Read File metadata
    greptitle = subprocess.Popen(["grep","Title"], stdin=parsefile.stdout,stdout=subprocess.PIPE)
    filetitle = greptitle.communicate()[0]
    filetitle = re.sub("Title=",'',filetitle.decode('UTF-8'))
    print(filetitle)

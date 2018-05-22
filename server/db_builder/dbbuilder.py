#!/usr/bin/env python3
import sqlite3
import os
import formic # This is a special Python 3 compatible version of Formic
import mutagen
import subprocess
import re
import time
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
    # Parsing the command and running GREP appears to need multiple pipes, look into fixing this later
    parsefile1 = subprocess.Popen(["mutagen-inspect", fname], stdout=subprocess.PIPE) # Read File metadata
    parsefile2 = subprocess.Popen(["mutagen-inspect", fname], stdout=subprocess.PIPE)  # Read File metadata
    parsefile3 = subprocess.Popen(["mutagen-inspect", fname], stdout=subprocess.PIPE)  # Read File metadata
    parsefile4 = subprocess.Popen(["mutagen-inspect", fname], stdout=subprocess.PIPE)  # Read File metadata
    # Grep Title
    greptitle = subprocess.Popen(["grep","Title"], stdin=parsefile1.stdout,stdout=subprocess.PIPE) # Grep Title
    filetitle = greptitle.communicate()[0]
    filetitle = re.sub("Title=",'',filetitle.decode('UTF-8'))
    # Grep Artist
    grepartist = subprocess.Popen(["grep", "Artist"], stdin=parsefile2.stdout, stdout=subprocess.PIPE)  # Grep Artist
    fileartist = grepartist.communicate()[0]
    fileartist = re.sub("Artist=", '', fileartist.decode('UTF-8'))
    # Grep Album
    grepalbum = subprocess.Popen(["grep", "Album"], stdin=parsefile3.stdout, stdout=subprocess.PIPE)  # Grep Album
    filealbum = grepalbum.communicate()[0]
    filealbum = re.sub("Album=", '', filealbum.decode('UTF-8'))
    # Grep Seconds
    grepseconds = subprocess.Popen(["grep", "seconds"], stdin=parsefile4.stdout, stdout=subprocess.PIPE)  # Grep Album
    fileseconds = grepseconds.communicate()[0]
    fileseconds = re.sub("[a-zA-z]", '', fileseconds.decode('UTF-8'))
    fileseconds = fileseconds.replace('-', '')
    fileseconds = fileseconds.replace(',', '')
    fileseconds = fileseconds.replace('/', '')
    fileseconds = fileseconds.replace('(', '')
    fileseconds = fileseconds.replace(')', '')
    fileseconds = fileseconds.replace(' ', '')
    print('TITLE', filetitle)
    print('ARTIST',fileartist)
    print('ALBUM',filealbum)
    print('LENGTH', fileseconds)
    cursor.execute('INSERT INTO songs VALUES (\'' + filetitle + '\',\'' + fileartist + '\',\'' + filealbum + '\',\'' + fileseconds + '\')')
    connect.commit()
connect.close()
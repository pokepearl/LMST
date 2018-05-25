#!/usr/bin/env python3
import sqlite3
import os
import formic # This is a special Python 3 compatible version of Formic
import mutagen
import subprocess
import re
import time
import urllib.parse
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
cursor.execute('DROP TABLE IF EXISTS song')
cursor.execute('CREATE TABLE song (id text,title text,artist text,album text,length text, genre text, path text)')
songindex = 0 # Variable for the song index in table
for fname in musiclist:  # Start Scraping info from songs and append to DB
    songindex = songindex + 1
    # Parsing the command and running GREP appears to need multiple pipes, look into fixing this later
    parsefile1 = subprocess.Popen(["mutagen-inspect", fname], stdout=subprocess.PIPE) # Read File metadata
    parsefile2 = subprocess.Popen(["mutagen-inspect", fname], stdout=subprocess.PIPE)  # Read File metadata
    parsefile3 = subprocess.Popen(["mutagen-inspect", fname], stdout=subprocess.PIPE)  # Read File metadata
    parsefile4 = subprocess.Popen(["mutagen-inspect", fname], stdout=subprocess.PIPE)  # Read File metadata
    parsefile5 = subprocess.Popen(["mutagen-inspect", fname], stdout=subprocess.PIPE)  # Read File metadata
    # Grep Title
    greptitle = subprocess.Popen(["grep","-i","Title"], stdin=parsefile1.stdout,stdout=subprocess.PIPE) # Grep Title
    filetitle = greptitle.communicate()[0]
    filetitle = re.sub("Title=",'',filetitle.decode('UTF-8'), re.IGNORECASE)
    filetitle = re.sub("TITLE=", '', filetitle, re.IGNORECASE)
    # Grep Artist
    grepartist = subprocess.Popen(["grep","-i", "Artist"], stdin=parsefile2.stdout, stdout=subprocess.PIPE)  # Grep Artist
    fileartist = grepartist.communicate()[0]
    fileartist = re.sub("ALBUMARTIST=.*", '', fileartist.decode('UTF-8'), re.IGNORECASE)
    fileartist = re.sub("Artist=", '', fileartist, re.IGNORECASE)
    fileartist = re.sub("ARTIST=", '', fileartist, re.IGNORECASE)
    # Grep Album
    grepalbum = subprocess.Popen(["grep","-i", "Album"], stdin=parsefile3.stdout, stdout=subprocess.PIPE)  # Grep Album
    filealbum = grepalbum.communicate()[0]
    filealbum = re.sub("ALBUMARTIST=.*", '', filealbum.decode('UTF-8'), re.IGNORECASE)
    filealbum = re.sub("Album=", '', filealbum, re.IGNORECASE)
    filealbum = re.sub("ALBUM=", '', filealbum, re.IGNORECASE)
    # Grep Seconds
    grepseconds = subprocess.Popen(["grep","-i", "seconds"], stdin=parsefile4.stdout, stdout=subprocess.PIPE)  # Grep Album
    fileseconds = grepseconds.communicate()[0]
    fileseconds = re.sub("[a-zA-z]", '', fileseconds.decode('UTF-8'))
    fileseconds = fileseconds.replace('-', '')
    fileseconds = fileseconds.replace(',', '')
    fileseconds = fileseconds.replace('/', '')
    fileseconds = fileseconds.replace('(', '')
    fileseconds = fileseconds.replace(')', '')
    fileseconds = fileseconds.replace(' ', '')
    # Grep Genre
    grepgenre = subprocess.Popen(["grep","-i", "Genre"], stdin=parsefile5.stdout, stdout=subprocess.PIPE)  # Grep Album
    filegenre = grepgenre.communicate()[0]
    filegenre = re.sub("Genre=", '', filegenre.decode('UTF-8'), re.IGNORECASE)
    # Get Path of file
    songfile = fname.replace(os.getcwd()+'/',"")
    #print('TITLE', filetitle)
    #print('ARTIST',fileartist)
    #print('ALBUM',filealbum)
    #print('LENGTH', fileseconds)
    #print('GENRE',filegenre)
    print(songfile)
    print(str(urllib.parse.quote(songfile)))
    cursor.execute('INSERT INTO song  VALUES (\'' + str(songindex) + '\',\'' + filetitle + '\',\'' + fileartist + '\',\'' + filealbum + '\',\'' + fileseconds + '\',\'' + filegenre  + '\',\'' + str(urllib.parse.quote(songfile))  + '\')')
    connect.commit()
connect.close()
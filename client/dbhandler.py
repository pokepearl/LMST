#!/usr/bin/env python3
import os
import urllib
import sqlite3
from confighandler import *
from mpvhandler import *
def downloaddb(host,folder,name,localdb):
    dburl = host+folder+name
    currentdir = os.getcwd()
    print('Downloading latest version of the Database from',dburl)
    try:
        urllib.request.urlretrieve(dburl, currentdir+localdb)
    except urllib.error.HTTPError:
        print('ERROR: Unable to download Database')
def readdb(type,index):
    conn = sqlite3.connect(readconfig("HTTP","dbname"))
    cursor = conn.cursor()
    if type == "song":
        for row in cursor.execute('SELECT * FROM song WHERE id = \''+index+'\''):
            url = readconfig("HTTP","host")+readconfig("HTTP","dbdirectory")+str(row[6])
            print('Now Playing:', row[0])
            print('Title:', row[1])
            print('Artist:', row[2])
            print('Album:',row[3])
            print('URL:',url)
            mpv_playhttp(url)
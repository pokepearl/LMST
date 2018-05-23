#!/usr/bin/env python3
import os
import urllib
def downloaddb(host,folder,name,localdb):
    dburl = host+folder+name
    currentdir = os.getcwd()
    print('Downloading latest version of the Database from',dburl)
    try:
        urllib.request.urlretrieve(dburl, currentdir+localdb)
    except urllib.error.HTTPError:
        print('ERROR: Unable to download Database')
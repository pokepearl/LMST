#!/usr/bin/env python3
import os
import urllib.request
def downloaddb(host,folder,name,localdb):
    dburl = host+"/"+folder+"/"+name
    currentdir = os.getcwd()
    print('Downloading latest version of the Database')
    urllib.request.urlretrieve(dburl, currentdir+localdb)
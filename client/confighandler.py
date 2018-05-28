#!/usr/bin/env python3
import configparser
import os
from appdirs import *
config = configparser.ConfigParser()
confpath = user_config_dir('LMST')
def createconfig():
    config = configparser.ConfigParser()
    if os.path.isfile(confpath+'/lmstconf.ini') == True:
        pass
    else:
        config['HTTP'] = {'host': 'http://',
                          'dbdirectory': '/cache/',
                          'dbname': 'lmst.db'}
        config['FILE'] = {'localdb': 'files/lmst.db'}
        with open(confpath+'/lmstconf.ini', 'w') as configfile:
            config.write(configfile)
def readconfig(section,field):
    config.read(confpath+'/lmstconf.ini')
    try:
        return config[section][field]
    except KeyError:
        return 'ERROR: Invalid Config Section or Field'
def writeconfig(section,field,value):
    config.read(confpath+'/lmstconf.ini')
    try:
        config[section][field] = value
    except KeyError:
        return 'ERROR: Invalid Config Section or Field'
    with open(confpath+'/lmstconf.ini', 'w') as configfile:
        config.write(configfile)
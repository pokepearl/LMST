#!/usr/bin/env python3
import configparser
import os
config = configparser.ConfigParser()
def createconfig():
    config = configparser.ConfigParser()
    if os.path.isfile('lmstconf.ini') == True:
        pass
    else:
        config['HTTP'] = {'host': 'localhost',
                          'dbdirectory': 'cache',
                          'dbname': 'lmst.db'}
        config['FILE'] = {'localdb': 'files/lmst.db'}
        with open('lmstconf.ini', 'w') as configfile:
            config.write(configfile)
def readconfig(section,field):
    config.read('lmstconf.ini')
    try:
        return config[section][field]
    except KeyError:
        return 'ERROR: Invalid Config Section or Field'
def writeconfig(section,field,value):
    config.read('lmstconf.ini')
    try:
        config[section][field] = value
    except KeyError:
        return 'ERROR: Invalid Config Section or Field'
    with open('lmstconf.ini', 'w') as configfile:
        config.write(configfile)
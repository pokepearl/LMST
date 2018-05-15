#!/usr/bin/env python3
import configparser
import os
def createconfig():
    config = configparser.ConfigParser()
    if os.path.isfile('lmstconf.ini') == True:
        pass
    else:
        config['HTTP'] = {'host': 'localhost',
                          'dbdirectory': 'cache',
                          'dbname': 'lmst.db'}
        with open('lmstconf.ini', 'w') as configfile:
            config.write(configfile)
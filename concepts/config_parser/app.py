"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

"""

import concepts.config_parser.config as cfg
# reading a normal dict to get config
print(cfg.creds.get("id"))
print(cfg.creds.get("pass"))
print(cfg.creds.get("pass34"))


### Write to a config file

import configparser
parser = configparser.ConfigParser()
parser.add_section('Manager')
parser.set('Manager', 'Name', 'Ashok Kulkarni')
parser.set('Manager', 'email', "[\"value\",doit]")
parser.set('Manager', 'password', 'secret')

parser.add_section('Vice Manager')
parser.set('Vice Manager', 'Name', "[value,doit]")

fp=open('test.cfg','w')
parser.write(fp)
fp.close()

# read a config file
p = configparser.ConfigParser()
p.read("test.cfg")
print(p.get("Manager","Email"))

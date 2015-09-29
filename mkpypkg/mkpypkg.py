#!/usr/bin/env python
# -*- coding: utf-8 -*-

static_string = """import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup("""

questions = {'name' :'please enter the project name ', 'version': 'please enter project version.. for example 1.0.0 ', \
             'author': 'please enter author name ','author_email':'please enter author e-mail ', \
             'description': 'please enter short description of the project ',\
             'license' : 'license under which you want to distribute this code. or example Gnu Publi License (GPL), MIT... etc ',\
             'keywords': 'please enter the keywords ',
             'url': 'please enter the project url ', 'packages':'packages in this project (comma seprated list) ',\
             'install_requires': 'the packages required to install this project (comma seprated list)  ' }

sequence = ['name' , 'version' , 'author', 'author_email', 'description', 'url', 'packages' , 'install_requires']

config= {}

confstr = "\n     "

for s in sequence:
    #config[s] = raw_input( ":: "+ questions[s])
    if s == 'install_requires' or s == 'packages':
        confstr = confstr + s+" = "+ str(raw_input( ":: "+ questions[s]).split(',')) +" ,\n     "
    elif s == 'description':
        confstr = confstr + s +' = ("'+ str(raw_input(':: '+ questions[s]))+'") , \n     '
    else:
        confstr = confstr + s+" = '"+ raw_input( ":: "+ questions[s]) +"' ,\n     "

confstr = confstr + "long_description=read('README'),\n     "


#print confstr

#print"\n\n\n\n this is the complete file \n\n\n\n\n"

print static_string + str(confstr)+ "\n  )"

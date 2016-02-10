#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


static_string = """import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open( fname).read()

setup("""

questions = {'name': ('please enter the project name ',
                      os.getcwd().split(os.sep)[-1]),

             'version': ('please enter project version.. for example 1.0.0 ',
                         '1.0.0', ),

             'author': ('please enter author name ', 'Author'),

             'author_email': ('please enter author e-mail ',
                              'author@something.com', ),

             'description': ('please enter short description of the project ',
                             'something about the project', '', ),

             'license': ('license under which you want to distribute this \
                          code. or example Gnu Publi License \
                          (GPL), MIT... etc ', 'GPLV3', ),

             'keywords': ('please enter the keywords ', ' ',),

             'url': ('please enter the project url ', 'www.something.com', ),

             'packages': ('packages in this project \
                           (comma seprated list) ', '', ),
             'install_requires': ('the packages required to install this \
                         project (comma seprated list)  ', '',),
             'scripts': ('the scripts in this package ', '',)
             }

sequence = ['name', 'version', 'author', 'author_email', 'description',
            'url', 'packages', 'install_requires', 'keywords', 'scripts']

config = {}


def getInput(text):
    temp = raw_input(":: " + questions[text][0])
    if temp == '':
        temp = questions[text][1]

    return temp


def getConfigInput():
    for s in sequence:
        if s == 'install_requires' or s == 'packages' or s == 'scripts':
            config[s] = " = " + str(getInput(s).split(',')) + ", \n    "

        elif s == 'description':
            config[s] = ' = ("' + getInput(s) + '") , \n    '

        else:
            config[s] = " = '" + getInput(s) + "' ,\n    "


def generateConfigString():
    confstr = "\n    "

    for s in sequence:
        confstr += s + config[s]

    confstr += "long_description = read('README'),\n    "
    print (static_string + str(confstr) + "\n  )")

    return static_string + str(confstr)


def writeSetup(confstr):
    f = open('setup.py', 'w')
    f.write(confstr + "\n  )")
    f.close()

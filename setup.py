import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(fname).read()

setup(
    name = 'mkpypkg' ,
    version = '1.0.0' ,
    author = 'girish joshi' ,
    author_email = 'girish946@gmail.com' ,
    description = ("tool to create python package") , 
    url = 'https://github.com/girish946/mkpypkg' ,
    packages = ['mkpypkg'], 
    install_requires = [''], 
    keywords = 'python package setup.py pip' ,
    scripts = ['mkpip'], 
    long_description = read('README.md'),
    
  )

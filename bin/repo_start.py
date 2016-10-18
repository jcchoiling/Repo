#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys

APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_DIR = APP_DIR + '/repo' 
LIB_DIR = APP_DIR + '/libs' 

sys.path.insert(0,APP_DIR)
sys.path.insert(1,REPO_DIR)
sys.path.insert(2,LIB_DIR)



"""
from repo.main import MyRepo #import method 1
import repo.main #import method 2

I choose import method 2 in this case

"""

import repo.main
import lib.commons

if __name__ == '__main__':
	r = repo.main.MyRepo()
	r.run()
	lib.commons.login()
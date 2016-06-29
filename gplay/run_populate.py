#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os, os.path

cmd = "../store-listing-toolkit/populate-v2.py metadata -platform android -prj-path . -sheet 1tPOZNM47rf3ERvVcMi2hyKHkt8fxTrsOhM9_2aCWQ6g -customized-metadata-path ../src/gplay/metadata"
print cmd
os.system(cmd)

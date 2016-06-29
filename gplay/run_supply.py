#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os, os.path

cmd = 'supply -j ../Developer-412b5ee99736.json -p com.senspark.pet.idle.clicker.games.hamster --skip_upload_apk true --skip_upload_images true --skip_upload_screenshots true'
print cmd
os.system(cmd)
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 13:28:54 2022

@author: joneszc
"""

import urllib3
#import json
#import boto3
http = urllib3.PoolManager()

inst_prof_url = "http://169.254.169.254/2014-11-05/meta-data/iam/security-credentials/"

r = http.request('GET', inst_prof_url)
prof_name = r.data.decode('utf-8').strip()
print(prof_name)

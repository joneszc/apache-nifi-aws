# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 13:25:43 2022

@author: joneszc
"""

import boto3
import get_boto_session
import awswrangler as wr

session = get_boto_session.get_session('DataEngineer')
for obj in wr.s3.list_objects('s3://data_char/', boto3_session=session):
    print(obj)

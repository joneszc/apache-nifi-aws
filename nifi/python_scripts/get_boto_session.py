# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 12:20:06 2022

@author: joneszc
"""

import urllib3
import json
import boto3
http = urllib3.PoolManager()
#prof_name = 'DataEngineer'

def get_instance_prof():
    inst_prof_url = "http://169.254.169.254/2014-11-05/meta-data/iam/security-credentials/"
    r = http.request('GET', inst_prof_url)
    prof_name = r.data.decode('utf-8').strip()
       
    return prof_name



def get_prof_creds(prof_name):
    url = "http://169.254.169.254/2014-11-05/meta-data/iam/security-credentials/" + prof_name
    r = http.request('GET', url)
    creds_data = json.loads(r.data.decode('utf-8'))
    
    return creds_data 



def get_session(prof_name=None):
    if not prof_name:
        prof_name=get_instance_prof()
        print("Collecting profile name..."+"\n"+prof_name)
    data = get_prof_creds(prof_name.strip())
    ACCESS_KEY = data['AccessKeyId']
    SECRET_KEY = data['SecretAccessKey']
    SESSION_TOKEN = data['Token']

    session = boto3.Session(
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        aws_session_token=SESSION_TOKEN,
        region_name='us-east-1'
    )
    
    return session


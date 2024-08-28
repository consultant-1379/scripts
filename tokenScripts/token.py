#!/usr/bin/env python

import sys
import subprocess
import re

f = open("/home/cloud-user/curl/Auto/tokenScripts/dirtyToken.txt", "r")#open dirty token
data = f.read()
m = re.findall(r"credentials\"\:\"(.*?)\"\,",data,re.DOTALL)#remove the everything in string but the token
print m
f.close()




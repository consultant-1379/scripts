#!/usr/bin/env python

import sys
import subprocess
import re

f = open("/home/cloud-user/curl/Auto/vnfScripts/dirtyVNF.txt", "r")#open dirty token
data = f.read()
m = re.findall(r"id\"\:(.*?)}}}",data,re.DOTALL)#remove the everything in string but the token
print m
f.close()

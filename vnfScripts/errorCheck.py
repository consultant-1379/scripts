#!/usr/bin/env python
import re
import sys  
import subprocess
import fileinput

f =open('/home/cloud-user/curl/Auto/vnfScripts/dirtyVNF.txt','r+')
ver = f.read()
if "ERROR" in ver:
        #v = re.findall(r"(.*?)",ver,re.DOTALL)
        print str(ver)
        #print less text if the token is corrent


#!/usr/bin/env python
import sys
import re
import subprocess
import fileinput
import re

file_object = open("/home/cloud-user/curl/Auto/tokenScripts/cleanToken.txt", "w") #write to clean token
subprocess.call(["python", "/home/cloud-user/curl/Auto/tokenScripts/token.py"], stdout=file_object)# run token.py

s = open("/home/cloud-user/curl/Auto/tokenScripts/cleanToken.txt").read()#removes the brackets that surrounds the output of token.py 
s = s.replace("['", "")
f = open("/home/cloud-user/curl/Auto/tokenScripts/cleanToken.txt", "w")#place output into cleanToken.txt
s = s.replace("']", "")
f = open("/home/cloud-user/curl/Auto/tokenScripts/cleanToken.txt", "w")
f.write(s)
f.close

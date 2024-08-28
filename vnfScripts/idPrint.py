#!/usr/bin/env python

import sys
import re
sys.stdout.flush()

#user_input = raw_input("Enter template name:")
#input = raw_input("enter")
#user_input = str(template)
f =open('/home/cloud-user/curl/Auto/vnfScripts/cleanId.txt','r+')#open cleanToken.txt

message = f.read()
message = message.rstrip()

q = open("/home/cloud-user/curl/Auto/vnfScripts/cleanTemp.txt",'r+')

template = q.read()
template = template.rstrip()
#print(+ str(template))

print ("export UPL_FNAME=\"" + str(template)+"\"" )
print ("export PACKAGE_ID=" + str(message))

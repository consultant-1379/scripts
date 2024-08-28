#!/usr/bin/env python

#import __future__ import print_function
import sys
import re
sys.stdout.flush()

f =open('/home/cloud-user/curl/Auto/tokenScripts/cleanToken.txt','r+')#open cleanToken.txt

message = f.read()
message = message.rstrip()


print("curl -X GET --header 'Accept: application/json' --header 'AuthToken:"+ str(message) +"\' --header \'Authorization: Basic ZWNtYWRtaW47Q2xvdWRBZG1pbjEyMw==\' --insecure \'https://131.160.159.241/ecm_service/vnfpackages\'")
#place whats in cleanToken.txt into the curl commanad


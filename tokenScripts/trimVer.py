#!/usr/bin/env python
import re
f =open('/home/cloud-user/curl/Auto/tokenScripts/saveVer.txt','r+')
ver = f.read()
if "SUCCESS" in ver: 
	v = re.findall(r"{\"reqStatus\":(.*?)\"}\,",ver,re.DOTALL)
	print (str(v) + "\nmore info in saveVer.txt")
	#print less text if the token is corrent
else:
	print ver
	#print the full incorrect token text string

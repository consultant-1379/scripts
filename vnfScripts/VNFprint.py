#!/usr/bin/env python

import sys
import re
sys.stdout.flush()

f =open('/home/cloud-user/curl/Auto/vnfScripts/vnfName.txt','r+')#open cleanToken.txt

name = f.read()
name = name.rstrip()

q = open("/home/cloud-user/curl/Auto/vnfScripts/vnfDis.txt",'r+')

discription = q.read()
discription = discription.rstrip()

a = open("/home/cloud-user/curl/Auto/vnfScripts/excVNF",'w')

#print ("export UPL_FNAME=\"" + str(template)+"\"" )
#print ("export PACKAGE_ID=" + str(message))
#print(str(name))
#print(str(discription))

print >> a,("curl --insecure --user \"ecmadmin:CloudAdmin123\" --header \"tenantId:ECM\" -o dirtyVNF.txt  --header \"Content-Type: application/json\" -X POST https://131.160.159.241:443/ecm_service/vnf_packages \--data \'{\"tenantName\":\"ECM\",\"fileName\":\""+ str(name)  +"\",\"name\":\""+ str(name) +"\",\"description\":\""+ str(discription) +" Description\",\"category\":\"vapp\",\"vendor\":\"Ericsson\",\"version\":\"2\",\"softwareVersion\":\"18.0\",\"isPublic\":false,\"deploymentManager\":\"EXTERNAL_VNFM\",\"packageFormat\":\"EXTERNAL_FORMAT\",\"vnfManagers\":[{\"id\":\"${VAPP_MANAGER_ID}\"}],\"userDefinedData\":{\"aString\":\"ETSI NFV SOL\",\"aNumber\":0.03,\"anArray\":[1,2,3],\"anObject\":{\"organization\":\"ETSI\"},\"isg\":\"NFV\",\"workingGroup\":\"SOL\"}}\'\n./writeTempName.py\n./removeBrackets.py\n./writeExports.py\n./sourceExports.bash\n./errorCheck.py")


#!/bin/bash

echo  "sourcing exportCommands.bash"
#source /home/cloud-user/curl/Auto/vnfScripts/exportCommands.sh
. exportCommands.bash
echo $UPL_FNAME
echo $PACKAGE_ID
./uploadVNFpackage 

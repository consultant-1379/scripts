#!/usr/bin/env python

import sys
import re
import subprocess
import fileinput
import re

file_object = open("/home/cloud-user/curl/Auto/vnfScripts/exportCommands.bash", "w")#open file curlAuthToken
subprocess.call(["python", "/home/cloud-user/curl/Auto/vnfScripts/idPrint.py"], stdout=file_object)#places output of toCheck.py into curlAuth

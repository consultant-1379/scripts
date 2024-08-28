#!/usr/bin/env python

import sys
import re
import subprocess
import fileinput
import re

file_object = open("/home/cloud-user/curl/Auto/tokenScripts/curlAuthToken", "w")#open file curlAuthToken
subprocess.call(["python", "/home/cloud-user/curl/Auto/tokenScripts/toCheck.py"], stdout=file_object)#places output of toCheck.py into curlAuth

#!/usr/bin/env python

import sys
fd = open("vnfName.txt","w")
input = raw_input("Enter VNF name:")
fd.write(input)

fl = open("vnfDis.txt","w")
input = raw_input("Enter VNF discription:")
fl.write(input)


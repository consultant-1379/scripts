#!/usr/bin/env python
import sys

#sys.stdout = open('cleanTemp.txt', 'w')
#print 'test'

#user_input = raw_input("Enter template name:")
#print(user_input)
#sys.stdout = open('cleanTemp.txt', 'w')


fd = open("cleanTemp.txt","w")
input = raw_input("Upload VNF package file name:")
fd.write(input)


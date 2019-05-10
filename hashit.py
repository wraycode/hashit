#!/usr/bin/env python

import hashlib

txt = raw_input("Enter string to convert to md5 ")
print(hashlib.md5(txt.encode('utf-8')).hexdigest())

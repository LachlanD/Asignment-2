#!/usr/bin/env python

import sys


f = open(sys.argv[1])

p=1
for l in f.readlines():
	sp = l.split()
	for t in sp[1:]:
		if t == '"S1"':
			print "NC_000913\t%d\t%d" %(p, p+16)
		p += 1

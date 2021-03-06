#!/usr/bin/env python

#Lachlan Dryburgh 188607
#COMP90016 Computational Genomics - Semester 1 2017
#Assignment 2

# Initalise transition matrix
trans = [[0.0 for i in range(19)] for j in range(19)]

# State names
trans[0][0] = ''
trans[0][18] = 'SN'
trans[18][0] = 'SN'
for i in range(1,18):
  trans[0][i] = 'S' + str(i)
  trans[i][0] = 'S' + str(i) 

# SN->SN
trans[18][18] = 0.998
# SN->S1
trans[18][1] = 0.002
# Si->Si+1 and S17->SN
for i in range(1,18):
  trans[i][i+1] = 1.000


base2int = {
    'a':0,
    'c':1,
    'g':2,
    't':3
}

# Create transition file
transition = open("transitions.txt", 'w')
for r in trans:
  first = True
  for c in r:
    if not first:
      transition.write("\t")
    transition.write(str(c))
    first = False
  transition.write("\n")

def b2int(base):
    return base2int[base]

f = open("sd_table.txt", 'r')

next(f)

# Initialise emissions matrix
emissions = [[0.0 for i in range(5)]for j in range(19)]

# Emission and State Names
emissions[0] = ['', 'A', 'C', 'G', 'T']
for i in range(1,18):
  emissions[i][0] = 'S' + str(i)
  
# Count emissions for S1-S17
counts = [[0 for i in range(4)] for j in range(17)]
for l in f:
 for i in range(17):
  counts[i][b2int(l[16+i])] += 1

# Emission probabilities
for i in range(17):
  s = sum(counts[i])
  for j in range(4):
    emissions[i+1][j+1] = counts[i][j]/float(s)

emissions[18] = ['SN', 0.25, 0.25, 0.25, 0.25]

# Write emissions file
emission = open("emissions.txt", 'w')

for l in emissions:
  first = True
  for c in l:
    if not first:
      emission.write("\t")
    emission.write(str(c))
    first = False
  emission.write("\n")

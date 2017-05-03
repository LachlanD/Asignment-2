#!/usr/bin/env Rscript

tr = read.delim("transitions.txt", '\t', header = T)
em = read.delim("emissions.txt", '\t', header = T)

states = tr[,1]
rownames(tr) = states
tr = tr[,-1]
em = em[,-1]
rownames(em) = states

bases = colnames(em)

#apply(em, 1, max)
#paste(bases[apply(em, 1, which.max)][2:18], collapse='')

seq = read.delim("seq.fa")

seq = seq[,1]
s = unlist(strsplit(paste(seq), ''))

library(HMM)

hmm = initHMM(states, bases, transProbs = data.matrix(tr), emissionProbs = data.matrix(em))

options(max.print=9999999)
viterbi(hmm, s)


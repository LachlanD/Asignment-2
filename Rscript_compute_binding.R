#!/usr/bin/env Rscript

# Load transition and emission files
tr = read.delim("transitions.txt", '\t', header = T)
em = read.delim("emissions.txt", '\t', header = T)

states = tr[,1]
rownames(tr) = states
tr = tr[,-1]
em = em[,-1]
rownames(em) = states

bases = colnames(em)

# Print out the probabilities and string
#apply(em, 1, max)[1:14]
#paste(bases[apply(em, 1, which.max)][1:14], collapse='')

seq = read.delim("seq.fa")

seq = seq[,1]
s = unlist(strsplit(paste(seq), ''))

library(HMM)

# Train the HMM
hmm = initHMM(states, bases, transProbs = data.matrix(tr), emissionProbs = data.matrix(em))


# Find the viterbi solution to sequence file
options(max.print=9999999)
viterbi(hmm, s)


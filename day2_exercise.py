# Write a script to print out the most common 7-mer and its GC 
# percentage from all the sequences in data/records.fa. 
# You are free to reuse your existing toolbox.
#
# The example FASTA file was adapted from: 
# Genome Biology DNA60 Bioinformatics Challenge.

import re
import sys
import math
import os
import argparse
import seq_toolbox as seq_toolbox

os.chdir("/Users/Luca/Documents/GIT/Python_programming-course_2017/exercises/day2-Mollan86")

file = open('data/records.fa')
sequences = file.read().splitlines()

del sequences[2::2]

i=0
for i in sequences:
	print seq_toolbox.calc_gc_percent(i)
	i = i+1
else:
	print "finished"


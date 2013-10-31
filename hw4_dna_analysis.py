# Name: Katrina Sayre
# Evergreen Login: saykat03
# Computer Science Foundations
# Programming as a Way of Life
# Homework 3: DNA analysis (Part 1)

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print "You must supply a file name as an argument when running this program."
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# Number of G and C nucleotides seen so far.
gc_count = 0

# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the bp is a G or a C,
    if bp == 'C' or bp == 'G':
        # increment the count of gc
        gc_count = gc_count + 1


# divide the gc_count by the total_count
gc_content = float(gc_count) / total_count

# Print the answer
print 'GC-content:', gc_content

# Total nucleotides seen so far.
total_count = 0
# Number of A and T nucleotides seen so far.
at_count = 0

# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the bp is a A or a T,
    if bp == 'A' or bp == 'T':
        # increment the count of AT
        at_count = at_count + 1


# divide the at_count by the total_count
at_content = float(at_count) / total_count

# Print the answer
print 'AT-content:', at_content

####################################
### Calculate each individual bp ###
####################################

#######
## G ##
#######

# Total nucleotides seen so far.
total_count = 0
# Number of G nucleotides seen so far.
g_count = 0

# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the bp is a G,
    if bp == 'G':
        # increment the count of g
        g_count = g_count + 1


# divide the g_count by the total_count
g_content = float(g_count) / total_count

# Print the answer
print 'G-content:', g_content


#######
## C ##
#######

# Total nucleotides seen so far.
total_count = 0
# Number of C nucleotides seen so far.
c_count = 0

# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the bp is a C,
    if bp == 'C':
        # increment the count of gc
        c_count = c_count + 1


# divide the c_count by the total_count
c_content = float(c_count) / total_count

# Print the answer
print 'C-content:', c_content


#######
## A ##
#######

# Total nucleotides seen so far.
total_count = 0
# Number of A nucleotides seen so far.
a_count = 0

# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the bp is a A,
    if bp == 'A':
        # increment the count of A
        a_count = a_count + 1


# divide the at_count by the total_count
a_content = float(a_count) / total_count

# Print the answer
print 'A-content:', a_content


#######
## T ##
#######

# Total nucleotides seen so far.
total_count = 0
# Number T nucleotides seen so far.
t_count = 0

# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the bp is a T,
    if bp == 'T':
        # increment the count of T
        t_count = t_count + 1


# divide the at_count by the total_count
t_content = float(t_count) / total_count

# Print the answer
print 'T-content:', t_content


################################################
### Calculate sum, total and sequence length ###
################################################

# Total nucleotides seen so far.
total_count = 0
# Number T,A, G, and C nucleotides seen so far.
tagc_count = 0

# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the bp is a T, A, G, or C
    if bp == 'T' or bp == 'A' or bp == 'G' or bp == 'C':
        # increment the count of T,A,G, and C
        tagc_count = tagc_count + 1

# divide the tagc_count by the total_count
tagc_content = float(tagc_count)

# Print the answer
print 'Sum Count:', float(tagc_content)
print 'Total Count:', total_count
print 'Sequence Length:', len(seq)


#############################
### Calculate GC/AT Ratio ###
#############################

# Total nucleotides seen so far.
total_count = 0
# Number of G and C nucleotides seen so far.
gc_count = 0

# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the bp is a G or a C,
    if bp == 'C' or bp == 'G':
        # increment the count of gc
        gc_count = gc_count + 1

# divide the gc_count by the total_count
gc_content = float(gc_count) / total_count

# Total nucleotides seen so far.
total_count = 0
# Number of A and T nucleotides seen so far.
at_count = 0

# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the bp is a A or a T,
    if bp == 'A' or bp == 'T':
        # increment the count of AT
        at_count = at_count + 1

# divide the at_count by the total_count
at_content = float(at_count) / total_count

# divide at_content by the gc_content to get the AT/GC ratio
atgc_ratio = float(at_content) / float(gc_content)

# Print the answer
print 'AT/GC Ratio:', atgc_ratio


###################################
### Calculate GC Classification ###
###################################

# Total nucleotides seen so far.
total_count = 0
# Number of G and C nucleotides seen so far.
gc_count = 0

# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the bp is a G or a C,
    if bp == 'C' or bp == 'G':
        # increment the count of gc
        gc_count = gc_count + 1


# divide the gc_count by the total_count
gc_content = float(gc_count) / total_count

if gc_content > 0.60:
    print 'GC classification: High'
    
if gc_content < 0.40:
        print 'GC classification: Low'
        
if gc_content > 0.40 and gc_content < 0.60:
            print 'GC Classification: Moderate'
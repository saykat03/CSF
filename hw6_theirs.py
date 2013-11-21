# Name: Katrina Sayre
# Evergreen Login: saykat03
# Computer Science Foundations
# Programming as a Way of Life
# Homework 6

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

###################################################
### Problem 4 #####################################
###################################################

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

def funk():
     things = float(42)
     return things
print funk()

a = funk()

print a

b = 43 

b = b == a

print d

###################################################
### Problem 3 #####################################
###################################################

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

def funk2():
  return 42

assert funk() == funk2()
print "affirmative"

A = funk()
B = funk2()

result = A == B

print "Results:", result

# true
# compared funk to funk2 and they did indeed return the same float

q = 'things'
r = 'other things'
s = 0

while s <= 2:
    s = s + 1
    
    if q == r:
        i = q == r
        print i, 'is just around the riverbend'
    else:
        pass
        
# things strings are different...

###################################################
### Problem 5 #####################################
###################################################

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

x = 42

y = x

print y

z = x = 'hallelujah'

print x

# x is changed a few times, and therefore not always the same.
# z is, however, always the same, as it was defined only once. 

###################################################
### Problem 6 #####################################
###################################################

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

t = 37 == 38

print t

t = 37 == 37

print t

###################################################
### Problem 7 #####################################
###################################################

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 7 solution follows:"

assert q == q
print "affirmative, what glory!"

assert funk() == 42
print "This amount of glory is unmatched. Well done, ole' sport, Well done, indeed."

###
### Collaboration
###

# the order of problem 3 and 4 were switched so that I could use a function defined in problem 4, in problem 3. 

# Collaborated with Whitney Barber


# Name: Ian Hooper
# Evergreen Login: hooian24
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                     # makes the math.sqrt function available
###
### Problem 1
###

print "Problem 1 solution follows:"
a = 1 
b = -5.86
c = 8.5408
solution1 = (-b + math.sqrt(pow(b,2) - (4*a*c)))/(2*1)

solution2 = (-b - math.sqrt(pow(b,2) - (4*a*c)))/(2*1)
print solution1


print solution2



print "Problem 2 solution follows:"

###Imports variables from the hw1_test frile for use        

import hw1_test
print hw1_test.a
print hw1_test.b
print hw1_test.c
print hw1_test.d
print hw1_test.e
print hw1_test.f




###
### Problem 3
###

print "Problem 3 solution follows:"

###Uses the Variables imported earlier and solves a boolean operation
 

print   ((hw1_test.a and hw1_test.b) or (not hw1_test.c) and not (hw1_test.d or hw1_test.e or hw1_test.f))


###
### Travis and Alejandro 
###

# ... List your collaborators here, as a comment (on a line starting with "#").

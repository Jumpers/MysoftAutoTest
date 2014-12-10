# -*- coding: utf-8 -*-

def add(a, b):
    print "Adding %d + %d " % (a, b)
    return a + b

def subtract(a, b):
    print "Subtracting %d - %d " % (a, b)
    return a - b

def device(a, b):
    print "Devicing %d / %d " % (a, b)
    return a / b 

def multiply(a, b):
    print "Multiplying %d * %d " % (a, b)
    return a * b

print "Let's do some math with just functions !"

age = add(10, 5)
height = subtract(19, 4)
weight = multiply(90, 2)
iq = device(100,2)

print "Age : %d , Height : %d ,Weight : %d ,IQ : %d " % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.

print "Here is a puzzle."

what = add(age, subtract(height,multiply(weight,device(iq, 2))))

print "That becomes:", what, "Can you do it by hand?"


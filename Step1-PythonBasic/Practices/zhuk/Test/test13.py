from sys import argv

script, first, second, third = argv

print "the script is called:", script
print "your first variable is:", first
print "your second variable is:", second
print "your third variable is:", third


#when more than 3 variable
#ValueError: too many values to unpack

#when less than 3 variable
#ValueError: need more than 2values to unpack
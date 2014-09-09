x = "There are %d types of people." %10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary,do_not)
z = True
a = "I love my home! %r"
b = "I love my home! %s"
c = "I love my home! %d"

print x
print y
print "I said: %r." %x
print "I said: '%r'."
print "I said: '%r'." %x

print "I also said: '%s'." %y
print "I also said: %s," %y

print z 
print x + y
# print x + % z
print a % z
print b % z
print c % z
# print c % binary  

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious
print joke_evaluation 

w = "This is the left side of ..."
e = "a string with a right side."

print w + e
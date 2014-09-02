# -*- coding:utf-8 -*-
#name = raw_input("What's your name?")
#if name.endswith('DT'):
#    print "Hello DT"
#elif name.endswith('dengt'):
#    print "Hello dengt"
#else:
#    print "Hello strange"


#练习1
#print "Hello World!"
#print "Hello Again"
#print "I like typing this"
#print "This is fun"
#print "Yay! printing"
#print "I'd much rather you 'not'. "
#print 'I "said" do not touch this.' 


#练习2
# A comment, this is so you can read your program later.
# Anything after the # is ignored by python.
#print "I could have code like this." # and the comment after is ignored
# You can also use a comment to "disable" or comment out a piece of code:
# print "This won't run."
#print "This will run" 


#练习3
#打印语句
#print "I will now count my chicken:"
#打印&计算
#print "Hens", 25+30/6
#打印&计算
#print "Roosters", 100-25*3%4
#print "Now I will count the eggs:"
#print 3+2+1-5+4%2-1/4+6
#print "Is it true that 3+2<5-7?"
#print 3+2<5-7
#print "What is 3+2?",3+2
#print "What is 5-7?",5-7
#print "Oh,that's why it's False."
#print "How about some more."
#print "Is it greater?",5>-2
#print "Is it greater or equal?",5>=-2
#print "Is it less or equal?",5<=-

#加分练习
#print "计算3234*29。43/23的结果"
#print "3234*29.43/23=",3234*29/23
#print "Is that right?",3234*29/23>=3234*29.43/23
#print "So what's the answer?",3234*29.43/23
#print 7%4

#练习4
#cars=100
#space_in_a_car=4.0
#drivers=30
#passengers=90
#cars_not_driven=cars-drivers
#cars_driven=drivers
#carpool_capacity=cars_driven*space_in_a_car
#average_passengers_per_car=passengers/cars_driven

#print "There are",cars,"cars available."
#print "There are only",drivers,"drivers available."
#print "There will be",cars_not_driven,"empty cars today."
#print "We can transport",carpool_capacity,"people today."
#print "We have",passengers,"to carpool today."
#print "We need to put about",average_passengers_per_car,"in each car."
#car_pool_capacity未定义
#加分练习
#print "enter the number of cars"
#cars=raw_input()
#print "enter the number of space_in_a_car"
#space_in_a_car=raw_input()
#print "enter the number of drivers"
#drivers=raw_input()
#print "enter the number of passengers"
#passengers=raw_input()
#cars_not_driven=cars-drivers
#cars_driven=drivers
#carpool_capacity=cars_driven*space_in_a_car
#average_passengers_per_car=passengers/cars_driven

#print "There are",cars,"cars available."
#print "There are only",drivers,"drivers available."
#print "There will be",cars_not_driven,"empty cars today."
#print "We can transport",carpool_capacity,"people today."
#print "We have",passengers,"to carpool today."
#print "We need to put about",average_passengers_per_car,"in each car."
#raw_input()捕获的是字符串


#练习5
my_name = 'Zed A.Shaw'
my_age = 35#not a lie
my_height = 74#inches
my_weight = 180 # lbs
my_eyes='Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(my_eyes,my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

#this line is tricky,try to get it exactly right
print "If I add %d,%d,and %d I get %d." %(
        my_age, my_height, my_weight,my_age + my_height + my_weight)
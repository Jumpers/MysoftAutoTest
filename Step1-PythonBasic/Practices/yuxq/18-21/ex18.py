def print_tow(*args):
    arg1,arg2=args
    print "arg1: %r, arg2: %r" % (arg1,arg2)

def print_tow_again(arg1,arg2):
    print "arg1: %r, arg2: %r" % (arg1,arg2)

def print_one(arg1): 
    print "arg1: %r" % arg1
    
def print_none():
    print "I got nothin'."
    
print_tow("zed","shaw")
print_tow_again("zed","shaw")
print_one("Frist!")
print_none()
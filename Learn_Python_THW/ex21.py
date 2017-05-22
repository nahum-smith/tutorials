def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some math with just some functions"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
IQ = divide(300, 2)

print "Age: %d, Weight: %d, Height: %d, IQ: %d" % (age, weight, height, IQ)

# a puzzle for the extra credit, type it anyway/
print "Here is a puzzle"

what = add(age, subtract(height, multiply(weight, divide(IQ, 2))))

print "That becomes: ", what, "Can you do it by hand?"

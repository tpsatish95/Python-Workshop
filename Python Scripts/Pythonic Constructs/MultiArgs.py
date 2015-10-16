# Normal Function Call
def myfunction(first, second, third):
    # do something with the 3 variables
    print(first + second + third)

myfunction(1, 2, 3)
# >> 6

def foo(first, second, third, *theRest):
    print "First: %s" % first
    print "Second: %s" % second
    print "Third: %s" % third
    print "And all the rest... %s" % list(theRest)

foo(1, 2, 3, 4, 5, 6, 7)
foo(1, 2, 3, 4, 5)


def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print "The sum is: %d" % (first + second + third)    # The sum is: 6

    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action="sum", number="first")
print "Result: %d" % result    # Result: 1

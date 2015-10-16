import re

line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print "matchObj.group() : %s " % matchObj.group()
    print "matchObj.group(1) : %s " % matchObj.group(1)
    print "matchObj.group(2) : %s " % matchObj.group(2)
else:
    print("No match!!")
# RESULT
# matchObj.group() : Cats are smarter than dogs
# matchObj.group(1) : Cats
# matchObj.group(2) : smarter

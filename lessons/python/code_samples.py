#indention level controls blocks
x = 3

if x < 10:
    print "small"
    print "number"
else:
    print "large"
    print "number"

# list comprhensions are a nice shortcut
l1 = []
for x in range(0,10):
    l1.append(x)

# is the same as....

l2 = [x for x in range(0,10)]

print l1, l2

#def foo(x, y, z=1)
    print x, y, z

foo(1,2)
foo(1,2,z

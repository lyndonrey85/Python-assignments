'''for i in range(0, 16):
        if i % 2 == 0:
            print "* " * 4
        else:
            print " *" * 4'''
def checkerboard(num):
    for i in range(0, num):
        if i % 2 == 0:
            print "* " * 4
        else:
            print " *" * 4
checkerboard(8)
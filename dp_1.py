from base import *

infile = open("C:\Users\wearable\it2.txt", "r")
infile2 = open("C:\Users\wearable\IT.txt", "r")

test1 = base(infile)
test1.start(35)
test1.filter(0.35, 45.0, 1000.0, 0.0)
test1.clear()
test2 = base(infile2)
test2.start(75)

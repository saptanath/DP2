from base import *
from compare import *

infile = open("C:\Users\wearable\emily.txt", "r")
#infile2 = open("C:\Users\wearable\IT.txt", "r")
oxy = []
oxy_1 = []
test1 = base(infile)
test1.clear()
oxy = test1.start()
oxy_1 = test1.filter(8, 550.0, 1000.0, 0.0)
test2 = compare(oxy, oxy_1, 30)
test2.xavier()
test2.clear()

#test2 = base(infile2)
#test2.start(75)

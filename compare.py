import matplotlib
import numpy as np
import matplotlib.pyplot as plt

import math 
from statistics import *
class compare:

	dork = []
	pork = []
	cork = []
	fork = []

	sock = 0.0
	lock = 0.0

	def __init__(self, mylist1, mylist2, ol):
		self.mylist1 = mylist1
		self.mylist2 = mylist2
		self.ol = ol

	def maximus (self, mylist3):
		i = 0
		j = 0
		k = 0
		temp = []
		mylist = []
		length = len(mylist3)-1
		while i < len(mylist3):
			temp.append(mylist3[i])
			j = j+1
			i = i+1
			if (j == self.ol or i == length):
				if(len(temp) == 1):
					j = 0
					temp=[]
				else:
					j = 0
					mylist.append(temp)
					k = k+1
					temp = []
		return mylist			

	def clear(self):
		self.dork[:] = [] 	
	
	def xavier (self):
		self.dork = self.maximus(self.mylist1)
		self.pork = self.maximus(self.mylist2)

		mars = statistics(self.mylist1)
		venus = statistics(self.mylist2)

		self.lock = mars.rootmean(self.mylist1, self.ol)
		self.cork = mars.stats(self.mylist1, self.ol) #standard devaition of original data points 

		self.sock = venus.rootmean(self.mylist2, self.ol)
		self.fork = venus.stats(self.mylist2, self.ol)  #standard deviation points for the filtered data points 

		#check if heart rate value is above 70, check the standard deviation, look at the filtered data, to dtermine if there was a sudden rise or
		#inconsistency on heart values such as a rapid wave. With each check the value to which standard deviation is compared to is changed. 
		
	def hitler (self, k):
	 	min1 = min(self.pork[k-1])
	 	mx1 = max(self.pork[k])
	 	merged = []
	 	merged = self.pork[k-1] + self.pork[k]
	 	jupiter = statistics(merged)
	 	i = merged.index(min(merged))
	 	while i <= merged.index(max(merged)):
	 		calcifer = jupiter.lineread(merged)
	 		i = i + 1


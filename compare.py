import math 
class compare:

	dork = []
	pork = []

	def __init__(self, mylist1, mylist2, ol):
		self.mylist1 = mylist1
		self.mylist2 = mylist2
		self.ol = ol

	def maximus (self):
		i = 0
		j = 0
		temp = []
		mylist = []
		length = len(self.mylist1)-1
		while i < len(self.mylist1):
			temp.append(self.mylist1[i])
			j = j+1
			i = i+1
			if (j == self.ol or i == length):
				if(len(temp) == 1):
					j = 0
					temp=[]
				else:
					j = 0
					mylist.append(temp)
					temp = []
		return mylist			

	def clear(self):
		self.dork[:] = [] 	
	
	def xavier (self):
		self.dork = self.maximus(mylist1)
		self.pork = self.maximus(mylist2)







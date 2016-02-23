def mymean (self, mylist):
		i = 0
		me = 0.0
		length = len(mylist)
		while i < len(mylist):
			me = me + mylist[i]
			i = i+1
	
		return me/(length)


def standardev (self, mylist):
	i = 0
	std = 0.0
	mea = self.mymean(mylist)
	while i < len(mylist):
		num = abs(mylist[i] - mea)
		num = math.pow(num, 2)
		std = std + num
		i = i + 1
	std = std/(len(mylist)-1)
	std = math.sqrt(std)
	return std


def stats (self, mylist, ol):
	i = 0
	j = 0
	temp = []
	stdx = []
	length = len(mylist)-1
	while i < len(mylist):
		temp.append(mylist[i])
		i = i+1
		j = j+1
		if (j == ol or i == length):
			if(len(temp) == 1):
				j=0
				temp=[]
			else:
				j = 0
				stdx.append(self.standardev(temp))
				temp =[]

		return stdx 
def difference (self, mylist):
	i = 0
	diff = []
	temp = self.mymean(mylist)
	while i < len(mylist):
		num = mylist[i] - temp
		num = abs(num)
		diff.append(num)
		temp = mylist[i]
		i = i+1
	
	return diff

def rootmean (self, mylist, ol):
	i = 0
	j = 0
	temp = []
	rootmeansq = []
	length = len(mylist)-1
	while i < len(mylist):
		temp.append(mylist[i])
		i = i+1
		j = j+1
		if (j == ol or i == length+1):
			if(len(temp) == 1):
				j=0
				temp=[]
			else:
				j = 0
				rootmeansq.append(self.rootmeansquare(temp))
				temp =[]
	return rootmeansq		

def rootmeansquare (self, mylist):
	rootmeansq = 0.0
	i = 0
	while i < len(mylist):
		rootmeansq = math.pow(mylist[i], 2) + rootmeansq
		i = i+1
	rootmeansq = math.sqrt(rootmeansq/(len(mylist)))
	return rootmeansq
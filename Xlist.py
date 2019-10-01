supplies=['book','handbook','pencile','pen','stapler','mobile','pendrive']
a=0
for i in range(len(supplies)):
	a+=1
	print(str(a)+" no. item is: "+supplies[i].title())
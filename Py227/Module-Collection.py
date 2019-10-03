from collections import OrderedDict
favorite_lan=OrderedDict()
favorite_lan['abcd']=1
favorite_lan['abd']=2
favorite_lan['ad']=3
favorite_lan['acd']=1+3
for x,y in favorite_lan.items() :
	print(x.title()+"'s favorite language is "+str(y))

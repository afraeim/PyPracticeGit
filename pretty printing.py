import pprint
msg='hey there, now you are working with pprint module!'
count={}
for n in msg:
	count.setdefault(n,0)
	count[n]=count[n]+1
pprint.pprint(count)	
a=input('Enter user name: ')
b=int(input('Enter total number of units: '))
if b<=100:
	c=b*1.75
	if not c<=100:
		if c>1000:
			c=c+(c*(15/100))
			print("Total charges with 15% VAT for {0} : {1} BDT".format(a,c))
		else:
			print('Total charges for {0} : {1} BDT'.format(a,c))	
	else:
		print('Note: All user chrged a minimum of tk. 100')	
elif b<=200:
	c=b*2.25
	if not c<=100:
		if c>1000:
			c=c+(c*(15/100))
			print("Total charges with 15% VAT for {0} : {1} BDT".format(a,c))
		else:
			print('Total charges for {0} : {1} BDT'.format(a,c))	
	else:
		print('Note: All user chrged a minimum of tk. 100')	
elif b>=300:
	c=b*3.50
	if not c<=100:
		if c>1000:
			c=c+(c*(15/100))
			print("Total charges with 15% VAT for {0} : {1} BDT".format(a,c))
		else:
			print('Total charges for {0} : {1} BDT'.format(a,c))	
	else:
		print('Note: All user chrged a minimum of tk. 100')	
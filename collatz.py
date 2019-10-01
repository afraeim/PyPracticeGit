def colltaz(number):
	if number%2==0:
		return number//2
	elif number%2==1:
		return 3*number+1
while True:		
	x=int(input("Enter number: "))	
	function=colltaz(x)
	print(function)		
	if function==1:
		break
#===========DONE============#		
print("Start")
a=str(input("Is it raining?"))
a=a.lower()
if a=='yes':
	b=str(input("Have umbrella?"))
	if b=="yes":
		print("Go outside.")
	else:	
		print("wait a while")
		c=str(input("Is it raining?"))
		while c=='yes':
			print("wait a while")
			c=str(input("Is it raining?"))
			continue
		print("Go outside.")	
else:
	print("Go outside.")
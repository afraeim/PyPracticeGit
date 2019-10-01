import random as rp
x=rp.randint(1,50)
print("I'm thinking of a number between 1-20")
try:
	for i in range(1,10):
		print("take a guess")
		guess=int(input())
		if guess<x:
			print('Your guess is too low')
		elif guess>x:
			print('Your guess is too high')
		else:
			break
	if guess==x:
		print('You are success at '+str(i))
	else:
		print("WRONG! it was ",str(x))			
except ValueError:
	print("You can't enter blank number!")		
				
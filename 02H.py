#def functionName(parameter):
#	job!

#like
def hello(parameter):
	print(parameter.title())
	print(parameter.title())
	print(parameter.title())
	print(parameter.title())

hello("abdul kader afraeim")		

import random as r
secretNumber=r.randint(1,10)
for guescount in range(1,6):
	guess=int(input("Give your guess: "))

	if guess>secretNumber:
		print("Your guess is too high!")
	elif guess<secretNumber:
		print("Your guess is too low!")
	else:
		break
if guess==secretNumber:
	print("Congrats! You guessed secret number at "
		+str(guescount)+" guesses!")
else:
	print("Nope. The number i was thinking is",secretNumber)					
	

def spam():
	global egg
	egg='hello'
	print(egg)
	
egg='hi'
egg='kash'
spam()
print(egg)

#X
spam=[['cat','bat'],['ball','football']]
print(spam[-1][0:-1])

#add values in list
spam[0]=['a','b','c']
print(spam)

del spam[1]
print(spam)
#String concataion 
a='hElLo'+' World'
print(a.casefold())

b=list(a)
print(len(b))
print('h' in a)

#X1
for i in range(0,100,5):
	print(i)
#range function work like 
a=[1,2,3,4,5]
for i in a:
	print(i)
#if i more explain 
for i in [1,2,3,4,5]:
	print(i)	
#List range
a=list(range(0,101,1))
print(a)

supplies=['pencile','stapler','book','page']
for i in range(len(supplies)):
	print(str(i)+" in supplies is : "+supplies[i])

#X2
#IN and NOT IN operators

myPets=['bangla-bilai','bideshi-bilai','japani-bilai']
pet=input("Enter a cat name: ")
if pet.lower() in myPets:
	print('I have this pet')
else:
	print("I don't have this pet")

#Multiple value assigenment trick	
#instade of
cat=['fat','black','loud']
size=cat[0]
color=cat[1]
disposition=cat[2]	
#i can write this
size,color,disposition=cat
print(size)
print(cat)
print(disposition)

#Finding the position in the list
**********PERSONAL PROJECT*******
import random
d=[]
r=random.randint(1,30)
for x in range(r):
	a=random.randint(1,50)
	d.append(a)	
print(d)
s=int(input("Number: "))
for d1 in d:
	if s==d1:
		print(d.index(s))
		print("nice")
	else:
		print("Beshi nice")		
**********PERSONAL PROJECT*********

#X4
spam=['a','b','c','d']
number=[1,2,4,7,9,20]
capital=["X","G","J","k"]
spam.remove("d")
spam.insert(3,'e')

print(spam)
del spam[-2]
spam+=capital
spam.sort(key=str.lower)
spam.sort(reverse=False)

print(spam)
















































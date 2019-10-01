import random
def getAnswer(number):
	if number==1:
		return 'It is one'
	if number==2:
		return 'It is two'
	if number==3:
	 	return "Okay it's three"
	if number==4:
		return "We are four"
	if number==5:
		return "We are prime FIVE"
	if number==6:
		return "----"
	if number==7:
		return "Lucky SEVEN"
	if number==8:
		return "magic8Ball"
for i in range(5):
	r=random.randint(1,8)
	print(getAnswer(r))						 			
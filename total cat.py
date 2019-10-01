cats=[]
while True:
	cat_name=str(input("Enter your "+str(len(cats)+1)+" cat name: "))
	cats.append(cat_name)
	if cat_name=='':
		del cats[-1]
		break
print("Cats name are: ")
i=0
for cat in cats:
	i+=1
	print(str(i)+" name is : "+cat)
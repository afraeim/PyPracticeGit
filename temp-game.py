print("HELLO THERE!\nThis program can calculate how many letter(Number/Alphabeting) is in text.\nPlease type your text.")
msg=input('Your text :')
count={}
for n in msg:
	count.setdefault(n,0)
	count[n]=count[n]+1
for v,k in count.items():
	print(str(v)+' : '+str(k))
import sys
# X is product code
# Y is quantity of this item
# DICTIONAR METHOD is useful here!
x,y=input().split()
x=int(x)
y=int(y)
if x==1:
	z=y*4.00
	print("Total: R$ "+"%.2f"%z)
elif x==2:
	z=y*4.50
	print("Total: R$ "+"%.2f"%z)
elif x==3:
	z=y*5.00
	print("Total: R$ "+"%.2f"%z)
elif x==4:
	z=y*2.00
	print("Total: R$ "+"%.2f"%z)
elif x==5:
	z=y*1.50
	print("Total: R$ "+"%.2f"%z)
else:
	sys.exit()
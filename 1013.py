a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
X=(a+b+abs(a-b))/2
Z=(X+c+abs(X-c))/2
print("%.0f"%Z,"eh o maior")
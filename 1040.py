#Game of List
X=list(map(int, input().split()))
#alternative: X = [int(x) for x in input().split()]
Z=sorted(X)
for d in Z:
	print(d)
print("")	
for g in X:
	print(g)
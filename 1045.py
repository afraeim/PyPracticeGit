X=list(map(int, input().split()))
s_hour=X[0]
s_minute=X[1]
e_hour=X[2]
e_minute=X[3]
if s_hour<e_hour:
	time=(e_hour-s_hour)
	if s_minute<e_minute:
		time_m=(e_minute-s_minute)
elif s_hour>e_hour:
	time=()
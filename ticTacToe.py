theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def pb(argument):
	print(argument['top-L']+'|'+argument['top-M']+'|'+argument['top-R'])
	print("-+-+-")
	print(argument['mid-L']+'|'+argument['mid-M']+'|'+argument['mid-R'])
	print("-+-+-")
	print(argument['low-L']+'|'+argument['low-M']+'|'+argument['low-R'])
sttr='X'
for i in range(9):
	print(pb(theBoard))
	print('Turn for '+sttr+'. Move on which space?')
	move=input()
	theBoard[move]=sttr
	if sttr=='X':
		sttr="O"
	else:
		sttr="X"
pb(theBoard)			
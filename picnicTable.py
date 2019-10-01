def panic(itemDic, right,left):
	print("Panic Item".center(right+left,'-'))
	for k,v in itemDic.items():
		print(k.ljust(right,'-')+str(v).rjust(left))
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 80}
panic(picnicItems,12,12)		
#removins white space by strip function
#strip have 3 types variation like,
#rstrip(), lstrip(), strip()
#Strip also can be use for removing alphabate or thing for text like
spam='eggeggballeggballeggegg'
print(spam.strip('egg'))
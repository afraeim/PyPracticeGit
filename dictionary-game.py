birthdays={
			'Alice':'Jan 1',
			'Bob':'Feb 1',
			'Cob':'Mar 1'
			}
while True:

	name=input("Enter a name: (Enter blank for quite)")
	if name=='':
		break
	if name in birthdays:
		print(name.title()+"'s birthday date is "+birthdays[name])
	else:
		print("Under this name no birthday information stored!\nDo you know? ")
		print("Enter 'Y' for yes & 'N' for no. ")
		flow=input(":")
		if flow=='N':
			break
		nwbday=input('Enter birthday date: ')
		birthdays[name]=nwbday.title()					
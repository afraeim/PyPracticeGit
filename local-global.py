def sp():
	global egg
	egg='chiken'#egg is global variable
def bacon():
	egg='bacon'#egg is local variable because in this scope eggs' value changed!
def ham():
	bacon()
	print(egg)#here egg is a local variable.
egg=42
print(egg)
sp()
ham()
print(egg)		
"""
#Conclusion i can access the global veriable from local scope. But local variable can't be access from global.
#local variable can access globaly if i use "global" key word in that local scope before the variable name.
***
1.In the spam() function, eggs is the global eggs variable, because there’s
a global statement for eggs at the beginning of the function. 
2.In bacon(), eggs is a local variable, because there’s an assignment statement for it in
that function. 
3.In ham(), eggs is the global variable, because there is no 
assignment statement or global statement for it in that function.
***

"""
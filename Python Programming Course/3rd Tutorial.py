

# a single line comment

# Multi Line Comments
'''
	this is a BLA BLA BLA 
	this is a BLA BLA BLA 
	this is a BLA BLA BLA 
'''


'''
	Variables : 
		Are containers for storing data values.
		Are created the moment you store data in them
		Naming a variable :
			1. don't start with a number  
			2. don't add some specific characters like -/*  
			3. don't add a white space 

'''



# Assign Value to Multiple Variables
x, y, t = 1, 2.5 ,"hhh"
print(x)
print(y)
print(t)

# We can also assign same value x = y = z = 5

# Concatenation
w = "There"
print("Hello "+w)

w = 5
print("number is "+str(w))


# Data Types
'''
	Text Type:	str
	Numeric Types:	int, float, complex
	Sequence Types:	list, tuple, range
	Mapping Type:	dict
	Set Types:	set, frozenset
	Boolean Type:	bool
	Binary Types:	bytes, bytearray, memoryview
'''
x = "Hello "	#str	
print(x)
x = 20	#int	
print(x)
x = 1.99	#float	
print(x)
x = 1j	#complex	
print(x)
x = ["a", "b", "c"]	#list	
print(x)
x = ("a", "b", "c")	#tuple	
print(x)
x = range(4)	#range	
print(x)
x = {"a" : "b", "c" : 36}	#dict	
print(x)
x = {"a", "b", "c"}	#set	
print(x)
x = frozenset({"a", "b", "c"})	#frozenset	
print(x)
x = True	#bool	
print(x)
x = b"Hello"	#bytes	
print(x)
x = bytearray(5)	#bytearray	
print(x)
x = memoryview(bytes(5)) #memoryview	
print(x)

# Getting the type of variable
x = 1j
print(type(x))
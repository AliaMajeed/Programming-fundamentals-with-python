# Languages 
# 1.High level( python ,java, c++ etc) & 2 .low level (0,1 forms)
# variable
#We can create any varibale , Variables are used to store data values. 
#how many functions are there which we can use with print function(SEARCHH)

# print output using print statement in terminal
print(5)
print("Hellow Python")
#Comments ; For understanding, Alwayz try to add comments in code where necessary
# two types of comments  1. with hash 2. with ''' 3.with """
#shortcut key ctrl /


 # multiline string variable we use tripple quotation
variable="""
print("Hellow Python")
print("Hellow Python")
print("Hellow Python")
"""

#Spacing:
# strip(): method used to remove extra spacing from start and end.
# split() : returnn every word separated with comma and add quotes to each word

variable = "   Hellow to python world   "
print(variable.split())
print(variable.strip())

#For Custom Spacing 
# 1. Use Join METHOD  ..... we can add or remove spacing form our  code oor text
variable = "   Hellow to python world   "
result = "   ".join(variable)  # Three spaces between words
print(result)

#2 variable.split() method......it removes space from start
variable = "   Hellow to python world   "
result = "   ".join(variable.split())  
print(result)


# #Repalce function
# variable = "   Hellow to python world   "
# result = "   ".join(variable.split())  
# print(result)
# string.replace(old, new, count)

variable= "Heloow this is our class"
replace=variable.replace("class", "class room")



text = "I have an apple and another apple."
result = text.replace("apple", "orange")
print(result)



#  Python has various data types including:

# String: Text enclosed in quotes. 
# Integer: Whole numbers.
# Float: Decimal numbers.
# Boolean: True or False.

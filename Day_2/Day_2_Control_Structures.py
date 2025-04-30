# Control Structures (Building Logic)

#1. Conditional Statements: if, elif, else
#2. Loops: for, while
#3. Loop Control Statements: break, continue, pass

#  1. Conditional Statements: if, elif, else
# These are used to execute code based on conditions.The syntax of these statements are as follows:

######## if Statement........Here only using if & Else

# if condition:
#     # code to run if condition is True
# else:
#     # code to run if condition is False

# ######## if/elif/else Statement..........Here using if, elif & else.

# if condition1:
#     # code to run if condition1 is True
# elif condition2:
#     # code to run if condition1 is False and condition2 is True
# else:
#     # code to run if both condition1 and condition2 are False


#Lets see an example of if/elif/else Statement
x = 10  #This assigns the value 10 to the variable x.

if x > 0:
    print("Positive number")
elif x == 0:
    print("Zero")
else:
    print("Negative number")

#Here we have 3 conditions to compare in this code
# if: checks the first condition.
# elif: (else if) checks another condition if the first is False.
# else: runs if none of the above conditions are True.


# 2. Loops: for, while
# Loops are used to repeat a block of code multiple times.

###### for Loop
# The for Loop is used to iterate over a sequence (like a list, string, or range).
for i in range(5):  # from 0 to 4
    print(i)


###### while Loop
# The while Loop is used to repeat a block of code multiple times. while Loop – repeats as long as a
#  condition is True.
count = 0
while count < 5:
    print(count)
    count += 1



# 3. Loop Control Statements: break, continue, pass
# These are used to control the flow of a loop.

###### break  exits the loop early.
for i in range(10):
    if i == 5:
        break  # loop stops at 5
    print(i)


######### Continue – skips the current iteration and continues with the next.
for i in range(5):
    if i == 2:
        continue  # skip when i == 2
    print(i)



######## Pass does nothing (placeholder for future code).
for i in range(3):
    if i == 1:
        pass  # nothing happens here
    print(i)

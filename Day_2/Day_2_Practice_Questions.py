# Practice Questions covering Control Flow
# 1.if, else, elif
# 2.Loops: for, while
# 3.Loop control: break, continue, pass


################Conditional Statements: if, elif, else#####################
#Problem 1: Even or Odd Checker
# Ask the user for a number and print whether it's even or odd.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# Problem 2: Leap Year Checker
# Write a Python program that checks whether a given year is a leap year or not.

Year = int(input("Enter a year: "))

if Year % 4 == 0:
    if Year % 100 == 0:
        if Year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")


#Problem 3 : Age Group Categorizer
# Take an age input and classify:
# 0–12: Child , 13–19: Teen , 20–59: Adult ,60+: Senior

age = int(input("Enter your age: "))

if age <= 12:
    print("Child")
elif age <= 19:
    print("Teen")
elif age <= 59:
    print("Adult")
else:
    print("Senior")


# Problem 4: Grade Calculator
# Input a score (0–100) and print:
# A: 90–100 ,B: 80–89 , C: 70–79 , D: 60–69 , F: below 60

score = int(input("Enter your score: "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")



# ############################Loops – for and while#######################

# Problem 5: Factorial Calculator
# Calculate the factorial of a number using a for loop.

num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial:", factorial)


# Problem 6: Fibonacci Series
# Print the Fibonacci series up to a given number using a while loop.

num = int(input("Enter a number: "))
a, b = 0, 1
while a < num:
    print(a)
    a, b = b, a + b

#Problem 7: Prime Number Checker
# Check if a number is prime or not using a while loop.

num = int(input("Enter a number: "))
is_prime = True
i = 2
while i < num:
    if num % i == 0:
        is_prime = False
        break
    i += 1
if is_prime:
    print("Prime number")
else:
    print("Not a prime number")

# Problem 8: Sum of First 10 Numbers
# Use a for loop to calculate the sum of numbers from 1 to 10.

sum = 0
for i in range(1, 11):
    sum += i
print("Sum:", sum)

# Problem 9: Sum of Even Numbers
# Use a while loop to calculate the sum of even numbers from 1 to 10.

sum = 0
i = 2
while i <= 10:
    sum += i
    i += 2
print("Sum:", sum)


#  Problem 10: Count Down
# Use a while loop to count down from 10 to 1 and print "Liftoff!" at the end.

i = 10
while i >= 1:
    print(i)
    i -= 1
print("Liftoff!")


# Problem 11: Multiplication Table
# Take an input number and print its table (up to 10) using a for loop.

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# #######################Loop Control – break, continue, pass

# Problem 12: Stop at Secret Word
# Keep asking the user for input in a loop. Stop (break) if they type "exit".

while True:
    word = input("Enter a word: ")
    if word == "exit":
        break


# Problem 13: Skip Even Numbers
# Use a loop to print numbers from 1 to 10, skipping even numbers (use continue).

for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)


# Problem 14: Placeholder Loop with pass
# Loop through a list of items. If an item is "TODO", just pass. Print the others.

items = ["apple", "banana", "cherry", "TODO", "date"]

for item in items:
    if item == "TODO":
        pass
    else:
        print(item)



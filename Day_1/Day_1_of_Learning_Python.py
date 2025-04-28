#Basics First (Syntax + Fundamentals)
# What is Python?
# Variables, Data Types
# Input/Output
# Basic Operators

# What is Python?...,Introduction
# Python is a popular programming language.
# It's used for web development, data science, automation, AI, and much more.
# It's known for being easy to read, easy to learn, and very powerful.

#1.First Python code using Print Statements	
print("Hello, World!")
#Comments ; For understanding, Alwayz try to add comments in code where necessary
# two types of comments  1. with hash 2. with ''' 3.with """
#shortcut key ctrl /

#2. Variables and Data Types
# Variables store data in memory to be used later.

name = "Alia"
age = 22
height = 5.6
is_student = True

#            Common Data Types:
#  Python has various data types including:
# String: Text enclosed in quotes.....written as str...."hello world"	
# Integer: Whole numbers(Integer numbers).....written as int....5, 100	etc.
# Float: Decimal numbers...written as float....3.14, 2.0 etc.
# Boolean: True or False...written as bool....True, False....Boolean (yes/no)

# 3. Input and Output
# Output: Showing something to the user. just like
print("Welcome to Python!")

# Input: Asking the user for information.just like
name = input("Enter your name: ")
print("Hello, " + name + "!")

# input() always gives a string. You may need to convert it if needed:
age = int(input("Enter your age: "))
print(age + 5)


# 4. Basic Operators
# Operator	             Example	                            Meaning
# +	                     3 + 2	                                Addition
# -	                     5 - 1	                                Subtraction
# *	                     4 * 3	                                Multiplication
# /	                     10 / 2	                                Division (float result)
# //	                 10 // 3	                            Division (integer result)
# %                      10 % 3	                                Modulus (remainder)
# **	                 2 ** 3	                                Exponent (power)

#Example Of  USING OPERTATORS
a = 10
b = 3
print(a + b)   # 13
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
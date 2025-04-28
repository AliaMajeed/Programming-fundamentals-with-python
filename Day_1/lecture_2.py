#Control Flow In python
# we give conditions to run our code so that it could fulfil our requirements compeletly. so we use conditions like (if , else , esle of , elif)
# grade = input("write your marks here")
# if grade >=80:
#     print("your grade is A")

# elif grade >=60:
#     print("your grade is B")

# elif grade >=40:
#     print("your grade is C")

# else :
#     print("you are failed")



# Data Structures  ....Lists (ordered, changeable, allows duplicates)

fruits = ['apple', 'banana', 'cherry']
print(fruits[0])  # 'apple'

#print (dir(fruits))....this will dispaly all the list methods .
pop_element=fruits.remove("banana")
print(pop_element)


for show in fruits:
    print(show)




names = ["ali", "ahmad", "Arsalan"]
ages = [22 ,30, 40]

for show in range(len(names)):
    print(f"the age of {names[show]} is {ages[show]}")
          # string kh ander kisi variable ko access krny kh liye formatted string yani f string use krty hyn


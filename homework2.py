'''
    GlobalAIHub - Homework 2
    Hüseyin ŞAHİN
    huseyinsahn@gmail.com
'''

first_name = input("Please enter user name: ")
last_name = input("Please enter user surname: ")
age = int(input("Please enter user age: "))
date_of_birth = int(input("Please enter user date of birth: "))

user = [first_name, last_name, age, date_of_birth]

for information in user:
    print(information)

if age < 0:
    print("Invalid age")
else:
    if age < 18:
        print("You can't go out because it's too dangerous.")
    else:
        print("You can go out to the street.")

'''
    GlobalAIHub - Homework 1
    Hüseyin ŞAHİN
    huseyinsahn@gmail.com
'''

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height: "))
is_married = bool(input("Please enter true if you are married, or false if you are not: "))
prime_numbers = list(input("Please enter prime numbers: "))

print("Entered name: ", name)
print("Type of name: ", type(name))

print(f"Entered age: {age}, Type of age: {type(age)}")

print("Entered height: {}".format(height))
print("Type of height: ", type(height))

print("Entered is_married: {} Type of is_married: {} ".format(is_married,type(is_married)))
print(f"Entered prime_numbers: {prime_numbers} Type of Value5: {type(prime_numbers)}")

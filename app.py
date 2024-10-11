# print('Hello world, welcome',100)
# print('welcome')

# variables
# name = 'Sheriff'
# age = 18
# print(name+' is a boy')
# print(name,'is 19', age)
# print(name+' is from America')

# strings
# print('Hi.\nHow are you doing')
# print('Hi.\'How are you doing\'')
# names = 'TEAM'
# print(names.lower().islower())
# print(names.index('A'))
# print(names.replace('T', 'R'))

# numbers
# number = 88
# number2 = str(number)
# print('number is ' + number2)
# print(43 - 33)
# print(20 % 3)
# print(abs(-7))
# print(max(2, 9, 17, 10))
# print(min(3, 1, 8 , 4, 9))
# print(round(3.5))
# print(bin(5))
# from math import *
# print(sqrt(100))

# input
# name = input('input your name: ')
# age = int(input('input your age: '))
# print('Your name is ' + name + ' and you' , age)

# word replacement excercise
# sentence = input('Enter your sentence: ')
# print('Your sentence is: '+sentence)
# word1 = input('Enter the word to replace: ')
# word2 = input('Enter the word to replace it with: ')
# print(sentence.replace(word1, word2))

# List
# Countries = ['America', 'Togo', 'Ghana', 'Nigeria', 'Australia']
# print(Countries[3][0])
# Countries = ['America', 'Togo', 'Ghana', 'Nigeria', 'Australia']
# print(Countries[2:])
# Countries = ['America', 'Togo', 'Ghana', 'Nigeria', 'Australia']
# print(Countries[1:4])
# Countries = ['America', 'Togo', 'Ghana', 'Nigeria', 'Australia']
# print(type(Countries))
# Countries = ['America', 'Togo', 'Ghana', 'Nigeria', 'Australia']
# print(Countries[-1])
# Countries = ['America', 'Togo', 'Ghana', 'Nigeria', 'Australia']
# print(len(Countries))
# Countries = ['America', 'Togo', 'Ghana', 'Nigeria', 'Austral1ia']
# Countries[0] = 'London'
# print(Countries)
# Countries = ['America', 'Togo', 2, 'Nigeria', 'True']
# print(type(Countries[2]))

# List Methods
# List1 = [1, 2, 3, 4, 5]
# List2 = ['Apples', 'Mango', 'Banana', 'Oranges']
# List1.extend(List2)
# print(List1)
# List1 = [1, 2, 3, 4, 5]
# List2 = ['Apples', 'Mango', 'Banana', 'Oranges']
# List2.append('Cherry')
# print(len(List2))
# List1 = [1, 2, 3, 4, 5]
# List2 = ['Apples', 'Mango', 'Banana', 'Oranges']
# List2.insert(1, 'Cherry')
# print(List2)
# List1 = [1, 2, 3, 4, 5]
# List2 = ['Apples', 'Mango', 'Banana', 'Oranges']
# List2.remove('Apples')
# print(List2)
# List1 = [1, 2, 3, 4, 5]
# List2 = ['Apples', 'Mango', 'Banana', 'Oranges']
# List2.clear()
# print(List2)
# List1 = [1, 2, 3, 4, 5]
# List2 = ['Apples', 'Mango', 'Banana', 'Oranges']
# print(List2.index('Mango'))
# List2 = ['Apples', 'Mango', 'Banana', 'Oranges', 'Apples']
# print(List2.count('Apples'))
# List1 = [4, 2, 5, 3, 1]
# List1.sort()
# print(List1)
# List2 = ['Apples', 'Mango', 'Banana', 'Oranges']
# List2.reverse()
# print(List2)
# List1 = [1, 2, 3, 4, 5]
# List2 = ['Apples', 'Mango', 'Banana', 'Oranges']
# List3 = List2.copy()
# print(List3)
# List2 = ['Apples', 'Mango', 'Banana', 'Oranges']
# List2.pop()
# print(List2)
# List2 = ['Apples', 'Mango', 'Banana', 'Oranges']
# List2.pop(1)
# print(List2)
# List2 = ['Apples', 'Mango', 'Banana', 'Oranges']
# del List2[0]
# print(List2)
# List2 = ['Apples', 'Mango', 'Banana', 'Oranges']
# del List2
# print(List2)

# Tuples
# three_numbers = (1, 2, 3)
# print(three_numbers)
# three_numbers = (1, 2, 3)
# print(three_numbers[1])
# three_numbers = (1, 2, 3, 1)
# print(len(three_numbers))
# three_numbers = (1, 2, 3, 1)
# print(type(three_numbers))
# strings = ('home', 'Land', 'earth')
# print(strings)
# boo = (True, False, True)
# print(boo)
# three_numbers = (1, 'home', 2, True, 3, 1)
# print(three_numbers)
# three_numbers = (1, 'home', 2, True, 3, 1)
# print(type(three_numbers[3]))

# Functions
# def greetings_function():
#     print('Welcome User')
# greetings_function()

# def greetings_function(name):
#     print('Welcome '+name)
# greetings_function('Sheriff')

# def greetings_function(name, age):
#     print('Welcome ' +name+ '. You are ' +str(age)+ ' Years old')
# greetings_function('Sheriff', 19)

# def greetings_function(*names):
#     print('Welcome ' +names[0])
# greetings_function('Sheriff', 'Tunji', 'Shegz')

# def greetings_function(name, age):
#     print('Welcome ' +name+ '. You are ' +str(age)+ ' Years old')
# name = input('Enter name: ')
# age = input('Enter age: ')
# greetings_function(name, age)

# The return keyword
# def my_function():
#     return 5 + 7
# print(my_function())

# def add_numbers(num1, num2):
#     return num1 + num2
# print(add_numbers(5, 8))

# def add_numbers(num1, num2):
#     return num1 + num2
# num1 = int(input('Enter 1st number: '))
# num2 = int(input('Enter 2st number: '))
# print(add_numbers(num1, num2))

# IF statement in python
# a = 5
# b = 2
# if a > b:
#     print(str(a)+ ' is greater than ' +str(b))

# a = 2
# b = 2
# if a == b:
#     print(str(a)+ ' is equal to ' +str(b))

# a = True
# b = 'good'
# if a == True:
#     print('a is equal to 2')
# elif a == False:
#     print('a is equal to false')
# else:
#     print('a is non of the two')

# a = False
# b = 'good'
# if a != True:
#     print('a is not equal to 2')
    
# a = 5
# b = 3
# if a >= b:
#     print('True')

# a = 6
# b = 4
# if a == b:
#     print('a is equal to b')
# else:
#     print('a is not equal to b')

# boy = True
# short = True
# if boy == True or short == False :
#     print('He is a boy and he is short')
# else:
#     print('none of the above')

# boy = True
# short = True
# if boy == True and short == False:
#     print('He is a boy and he is short')
# else:
#     print('none of the above')

# value = input('input your value: ')
# if type(value) == str:
#     print(value, ' is a string')
# else:
#     print(value, ' is not a string')

# Building an Even number checker program 
# num = int(input('Enter a number: '))
# if num%2 == 0:
#     print('Even Number')
# else:
#     print('Odd Number')


# Dictionaries

# my_dict = {
#     'Name': 'Sheriff',
#     'Nationality': 'Africa',
#     'Qualification': 'BSC'
# }
# print(my_dict)

# my_dict = {
#     'Name': 'Sheriff',
#     'Nationality': 'Africa',
#     'Qualification': 'BSC'
# }
# print(my_dict['Name'])

# my_dict = {
#     'Name': 'Sheriff',
#     'Name2': 'Sheriff',
#     'Nationality': 'Africa',
#     'Qualification': 'BSC'
# }
# print(my_dict)

# my_dict = {
#     'Name': 'Sheriff',
#     'Name2': 'Sheriff',
#     'Nationality': 'Africa',
#     'Qualification': 'BSC'
# }
# print(len(my_dict))

# my_dict = {
#     'Name': 'Sheriff',
#     'Age': 19,
#     'is_tall': True,
#     'Nationality': 'Africa',
#     'Qualification': 'BSC'
# }
# print(my_dict['is_tall'])

# my_dict = {
#     'Name': 'Sheriff',
#     'Age': 19,
#     'is_tall': True,
#     'Nationality': 'Africa',
#     'Qualification': 'BSC',
#     'Friends': ['olamide', 'badoo', 'wizkid']
# }
# print(my_dict['Friends'])

# my_dict = {
#     'Name': 'Sheriff',
#     'Age': 19,
#     'is_tall': True,
#     'Nationality': 'Africa',
#     'Qualification': 'BSC',
#     'Friends': ['olamide', 'badoo', 'wizkid']
# }
# print(type(my_dict))

# my_dict = {
#     'Name': 'Sheriff',
#     'Age': 19,
#     'is_tall': True,
#     'Nationality': 'Africa',
#     'Qualification': 'BSC',
#     'Friends': ['olamide', 'badoo', 'wizkid']
# }
# x = my_dict['Name']
# print(x)


# While loop
# i = 1
# while i < 6:
#     print(i)
#     i += 1

# i = 1
# while i < 6 or i == 6:
#     print(i)
#     i += 1

# i = 10
# while i < 16 and i == 10:
#     print(i)
#     i += 1

# For loops in Python

# for Letters in 'Hello':
#     print(Letters)

# my_list = ['money', 'health', 'islam']
# for values in my_list:
#     print(values)

# my_dict = {
#     'name': 'shegz',
#     'age': 19
# }
# for values in my_dict:
#     print(values)

# my_list = ['money', 'health', 'islam', 'things']
# for values in my_list:
#     print(values)
#     if values == 'islam':
#         break

# my_list = ['money', 'health', 'islam', 'things']
# for values in my_list:
#     if values == 'islam':
#         break
#     print(values)

# for y in range(5):
#     print(y)

# for y in range(6, 11):
#     print(y)

# for z in range(7):
#     print(z)
# else:
#     print('Finished Looping')

# 2D LIST & NESTED LOOPS
# my_list = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(my_list)

# my_list = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(my_list[0][1])

# my_list = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for list in my_list:
#     for row in list:
#         print(row)


# Building a Basic Calculator

# num1 = int(input('Enter first number: '))
# num2 = int(input('Enter second number: '))
# op = input('Enter operator: ')

# if op == '+':
#     value = num1 + num2
#     print(value)
# elif op == '*':
#     value = num1 * num2
#     print(value)
# elif op == '/':
#     value = num1 / num2
#     print(value)
# elif op == '-':
#     value = num1 - num2
#     print(value)
# else:
#     print('invalid operator')


# Try Except in Python
# try:
#     x = int(input('Input an integer: '))
#     print(x)
# except:
#     print('somthing went wrong... pls try again')

# try:
#     x = int(input('Input an integer: '))
#     print(x)
# except ValueError:
#     print('Value is not an integer')

# try:
#     x = int(input('Input an integer: '))
#     print(x)
# except:
#     print('somthing went wrong')
# else:
#     print('nothing went wrong')

# try:
#     x = int(input('Input an integer: '))
#     print(x)
# except:
#     print('somthing went wrong')
# finally:
#     print('try except finished')


# READ FILES
# open ('countries.txt', 'r') read only
# open ('countries.txt', 'w') write & edit
# open ('countries.txt', 'a') append
# open ('countries.txt', 'r+') read and write

# coun_file = open ('countries.txt', 'r')
# print(coun_file.readable())
# coun_file.close()

# coun_file = open ('countries.txt', 'r')
# print(coun_file.readline())
# print(coun_file.readline())
# coun_file.close()

# coun_file = open ('countries.txt', 'r')
# print(coun_file.readlines())
# coun_file.close()

# coun_file = open ('countries.txt', 'r')
# print(coun_file.readlines()[3])
# coun_file.close()

# coun_file = open ('countries.txt', 'r')
# for lines in coun_file.readlines():
#     print(lines)
# coun_file.close()


# WRITING FILES
# New_File = open('New-File.txt', 'w')
# New_File.write('This is a new file')

# New_File = open('New-File.txt', 'a')
# New_File.write('\nThis is a new line')

# New_File = open('New-Python.py', 'w')
# New_File.write('print(\'This is a new file\')')


# Classes & Objects in Python

# class Myclass:
#     x = 5

# p1 = Myclass
# print(p1.x)

# class Person:
#     def __init__ (self, name, age):
#         self.name = name
#         self.age = age

# y1 = Person('Sheriff', 19)
# print(y1.name)
# print(y1.age)

# class Person:
#     def __init__ (self, name, age):
#         self.name = name
#         self.age = age
# name = input('Enter your name: ')
# age = input('Enter your age: ')

# z1 = Person(name, age)
# print(z1.name)
# print(z1.age)

# class Person:
#     def __init__ (self, name, age):
#         self.name = name
#         self.age = age

# y1 = Person('Sheriff', 19)
# del y1.age
# print(y1.age)

# class Person:
#     def __init__ (self, name, age):
#         self.name = name
#         self.age = age

# y1 = Person('Sheriff', 19)
# del y1
# print(y1)

# class Gold:
#     pass

# Inheritance in python
# from new import Student

# class Person(Student):
#     pass
# p1 = Person()
# print(p1.name)

# Building a simple login and signup system

# print('Creat your account')
# username = input('Input your username: ')
# password = input('Input your password: ')
# print('user ' + username + ' created sucessfully')
# print('Login now')
# confirm_name = input('Input username: ')
# confirm_password = input('Input password: ')
# if confirm_name == username and confirm_password == password:
#     print('user logged in sucessfully')
# else:
#     print('Invalid credentials')

# Modules and PIP in python
# import new

# new.say_hi()











































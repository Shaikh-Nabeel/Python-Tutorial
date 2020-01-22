# var= int(input())
# print(var)
# if var > 4:
#     print("Variable is g5reat")
# elif var == 3:
#     print("variable is three")
# else:
#     print("Variable is not great")


# it's not imp to write i=i+1 in for loop
# for i in range(0, 20):
#     print(i)

# it's  imp to write i=i+1 in while loop

# to make a function
# def average(num1, num2):
#     avr= (num1+num2)/2
#     return avr
#
# print(average(3,6))

# to keep running your program while error
# index=3
# try:
#     print(index)
#
# except Exception as e:
#     print(e)

# #to create a file
# f= open("nabsN.txt", "w")
# f.write("this file is created with python by Nabs")
# f.close()

# to read the file only
# f= open("nabsN.txt", "r")
# content =f.read()
# f.close()
# print(content)

# to print x to the power 10
# x= 4e3
# print(x)

# to add complex number
# a=5+4j
# b=3+2j
# print(a+b)
# To get the cube of number and ** this opr. is for power

# import math
# a= int(input("Enter Integer to  get cube root "))
# print(a**(1/3))

# To evaluate all type of Integer
# a=eval(input())
# print(a)
# print(a)

# pass is used when program is to be written in future
# for i in range(0, 10):
#     pass

# print('''shaikh''')

# loop
# for i in range(0, 5):
#     for f in range(0, i):
#         print("*", end=" ")
#     print()
#
# for i in range(0, 10):
#     if i % 2== 0:
#         print(i)

# prime number program
# a = int(input("Enter the number : "))
# b = True
# for i in range(2, a):
#     if a % i == 0:
#         b= False
#         break
# print(b)

# prime number by different method
# n = int(input())
# count =0
# for i in range(1, n+1, 1):
#     if (n % i == 0):
#         count +=1
# if(count==2):
#     print("prime no.")
# else:
#     print("not prime")

# String can be multiplied
# x="  nabs  shaikh   "
# print(x*2, end=" ")
# print(x[-1])
# print(x[1:3])
# print(x[::2])
# print(x[0:9:2])
# print(x[::-1]) # to reverse the string
# print(x.isalpha())
# print(x.isdigit())
# print(x.islower())
# print(x.upper())

# remove trailing space and leading space
# x=x.lstrip()
# print(x.rstrip())

# this function print ascii number
# print(ord('A'))

# this function take ascii number and give us value
# print(chr(97))

# # you can use any word in the place of wht
# for wht in 'shaikh':
#    print(wht*2, end=" ")

# to create list
# name_list =["shaikh", "nabs", "python", 786, "shaikh"]
# print(name_list)
# print(name_list[1])
# name_list.append("hello")
# print(name_list)
# print(name_list[2:4])

# name_list.insert(2, "python3")
# print(name_list)

# del name_list[3]
# print(name_list)
# name_list.reverse()
# print(name_list)

# print(name_list.index("shaikh"))
# print(name_list.count("shaikh"))
# print(len(name_list))
# print(max(name_list), min(name_list))
# print(sum(name_list))

# we can use for loop in list
# for item in ["swift", "audi", "ferrari"]:
#     print(item)


# loop list
# pow2=[2**x for x in range(11) if x % 2== 0]
# print("power of 2 from 1 to 10: ", pow2)

# tuples made by () this bracket. this is optional but we should apply , it cannot be changed once created
# b=(3, 7, 4)
# c = 1, 5, 3, 4, 7
# print(b)
# print(c)
# print(c[-1:-3:-1])
# loop in tuple
# for i in range(len(c)):
#     print(c[i]*2)
# print(max(c), min(c))

# creating tuple of only one element
# d= (1, )
# print(d)

# about dictionary
# dict1 = {1: 'nabs', 2: 'shaikh', 3: 'python'}
# marks={'Nabs': 80, 'Nirbhay': 85, 'Sameer': 80}
# print(dict1[1])
# print(marks['Nabs'])
# print(marks['Nirbhay'])
# marks['Sameer']= 85
# print(marks)

# to add any name and delete .
# marks['aman']=90
# print(marks)
# del marks['aman']
# print(marks)

# for key1 in marks:
#     print(key1)

# copy make reference
# Y =marks.copy()
# print(Y)

# items = marks.items()
# print(items)

# keys = marks.keys()
# print(keys)

# val = marks.values()
# print(val)

# a={1: 2, 2: 3}
# b={3: 5, 2: 4}
# c= a.update(b)
# print(a)

# bubble sort

# a= [8, 4, 1, 3, 2, 6]
# count=0
# for i in range(len(a)):
#     for j in range(1, len(a)):
#         if a[j-1]> a[j]:
#             count +=1
#             a[j-1], a[j] = a[j], a[j-1]
# print(a)
# print(count)
# it count no. of swapping

# insertion sort

# a= [8, 4, 1, 3, 2, 6]
# for i in range(len(a)):
#     minInd = i
#     for j in range(i, len(a)):
#         if a[j] < a[minInd]:
#             minInd = j
#     a[i], a[minInd] = a[minInd], a[i]
# print(a)

# first one is digit to be round off and second one is to how many place.
# a=66.657
# print(round(a, 2))
# print(round(a, -1))

# import math
# from math import factorial
# print(math.factorial(5))

# random module give random values for ex if u want to game of die roll
# import random
# right is inclusive
# print(random.randrange(1, 7))

# both are inclusive
# print(random.randint(1, 6))

# random choice
# direction =['south', 'north', 'east', 'west']
# print(random.choice(direction))
# random.shuffle(direction)
# print(direction)

# to get random decimal number between 0 and 100
# rand = random.random() *100
# print(rand)

# this greet function is made by user in idle so here we can import
# from functions import greet
# greet()

# TO DEFINE A FUNCTION
# import math

# def get_power(a, b):
#     return math.pow(a, b)

# print(get_power(b=3, a=4))
# print(get_power(3, 4))

# def cal(*name):
#     for i in name:
#         print("hello ", i)
#
# cal("nabs", "shaikh", "python")

# palindrome number

# a=int(input("Enter the number "))
# temp = a
# rev = 0
# while temp > 0:
#     last = temp % 10
#     rev = rev*10 +last
#     temp = temp//10
#
# if a==rev:
#     print("palindrome")
# else:
#     print("not palindrome")

# factorial
#
# def factorial(n):
#     """
#         we can write doc string in function like this
#         :param n: integer
#         :return: factorial of x
#      """
#     if n==1:
#         return 1
#     return n*factorial(n-1)
#
#
# print(factorial(5))


# binary search is method to reduce the time limit

# a = [1, 5, 6, 7, 8, 9, 11]
#
#
# def binary_search(a, key, start, end):
#
#     if start <= end:
#         mid = int((start+end) / 2)
#         if a[mid] > key:
#             return binary_search(a, key, start, mid-1)
#         elif a[mid] < key:
#             return binary_search(a, key, mid+1, end)
#         else:
#             return mid
#     print(key, "could not be found")
#     return -1
#
#
# print(binary_search(a, 8, 0, len(a)-1))


# this package is made by user in idle
# from my_package import sum_module
# print(sum_module.sum(45, 25))

# about date and time

# import datetime
# print(datetime.date.today())
# print(datetime.date.today().month)
# print(datetime.date.today().year)
# print(datetime.date.today().day)
# print(datetime.datetime.now().hour)
# print(datetime.datetime.now().minute)
# print(datetime.datetime.now().second)

# both function are same (given below)
# print(datetime.datetime.now())
# print(datetime.datetime.today())


# checking time || efficient algorithm

# import time
#
# n=10000
# start = time.time()
# sum1 = 0
# for i in range(1, n+1):
#     sum1 += i
#
# print(sum1)
# end = time.time()
# print(end - start)
#
# start = time.time()
# sum1 = (n * (n+1)) / 2
# print(sum1)
# end = time.time()
# print(end - start)


# stacks , in stack the element entered last in list will pop first

# a = [7, 5, 8, 4]
# a.pop()
# print(a)
#
# a.append(8)
# a.append(7)
# print(a)
#
# a.pop()
# a.pop(1)
# print(a)

# queue , in queue the element entered first in list will pop first

# b = [9, 8, 5, 3, 1]
# b.pop(0)
# b.pop()
# b.append(6)
# print(b)

# graph in python

import matplotlib.pyplot as plt

# x=[4, 5, 6, 7]
# y=[2, 25, 6, 27]
# plt.plot(x, y, 'r--')
# plt.plot(y, x, 'b')
# plt.xlabel('time')
# plt.ylabel('velocity')
# plt.title('Constant Acceleration')
# plt.show()


# x=[i for i in range(10)]
# y=[i*i*i for i in range(10, 20)]
# z=[i*2 for i in range(10, 20)]
# plt.subplot(2, 1, 1)
# plt.plot(x, y)
#
# plt.subplot(2, 1, 2)
# plt.plot(x, z, 'r')
#
# plt.show()

import numpy as np

# graph of sin
# x = np.arange(-10, 10, 0.1)
# y = np.sin(x)
# plt.plot(x, y)
# plt.show()

# Quadratic eq. graph
# x = np.arange(-10, 10, 0.1)
# y = x*x+2*x+5
# plt.plot(x, y)
# plt.show()

# BAR GRAPH
# x=[i for i in range(10)]
# x2=[i+0.3 for i in range(10)]
# y=[4,3,4,5,6,9,7,6,5,10]
# z=[9,7,6,5,10,4,3,4,5,6]
# plt.bar(x, y, color="blue",  width=0.3, label="2017")
# plt.bar(x2, z, color="red", width=0.3, label="2018")
# plt.legend()
# plt.show()


# PIE CHART

# hours = [2, 4, 8, 3, 5, 2]
# activity =["ready", "coaching", "school", "rest", "sleep", "tv"]
# explodes=[0.2,0,0,0,0,0,]
# plt.pie(hours, labels=activity, shadow="true", explode=explodes)
# plt.show()


# dictionary of four words
# a = input("Enter the word here: ")
dict3 = {'scary': 'frightening, causing fear.', 'abhor': 'regard with disgust and hatred', 'beautiful': 'looking good',
         'sophisticated': 'having or showing a lot of experience'}
# print("The meaning of", a, "is", dict3[a])


# about set in python
# s= set()
# print(type(s))

# s_from_list = set([1, 2, 3, 4])
# print(s_from_list)

# set will print only common values , no value will be printed twice
# we can also print max of set and min of set ans len as well
# s.add(1)
# s.add(1)
# s.add(2)
# s.remove(2)

# this line will print union of two sets
# s1 = s.union({1, 3})
# this line will print intersection of two sets
# s2 = s.intersection({1, 2, 3, 4})
# print(s, s1)
# print(s, s2)

# disjoint function (no value matched)
# s_4 = {4, 6}
# print(s.isdisjoint(s_4))
# sets overrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr

# a = int(input("Enter the first number; "))
# b = int(input("Enter the second number; "))
# c =input("Enter add, sub, multi, div for operations: ")
#
#
# if a == 56 and b == 4 and c == "add":
#     print("76")
# elif a== 45 and b== 3 and c== "multi":
#     print(555)
# elif a ==5 and b== 6 and c=="div":
#     print(4)
# elif c == "add":
#     print(a+b)
# elif c== "sub":
#     print(a-b)
# elif c== "multi":
#     print(a*b)
# elif c == "div":
#     print(a/b)
# else:
#     print("unknown number")

# assignment : to print only integer value from list
# faltu = 4
# list_try = ["nabs", 4, 5, 9, "python", 30, "nabs", 1005]
#
# for i in range(len(list_try)):
#     if type(list_try[i]) == type(faltu):
#         if list_try[i] > 6:
#             print(list_try[i])

# function


# def avrg(a, b):
#     """this is docstring"""
#
#     return (a+b)/2
#
#
# print(avrg(5, 7))

# try and except
# this program will try to excute the input but if input is wrong it will print exception

# num1= input("Enter : ")
#
# try:
#     print(int(num1))
# except:
#     print("hello, python user")

# exception as e

# num1= input("Enter : ")
#
# try:
#     print(int(num1))
#
# # this line will print problem of try but program will run
# except Exception as e:
#     print(e)
# print("hello, python user")

# to know file handling reading writing go to file-handling program

# fibonacci number
# a=1
# b=0
# for i in range(5):
#     c = a + b
#     b = a
#     a = c
#     print(c, end=" ")

# anonymous function or lambda function

# minus = lambda x, y: x-y

# we can also write above program in function
# def minus(x, y):
#     return x-y

# print(minus(4, 1))

# import sklearn   this module is use for machine learning

"""
we use args and kwargs in python like this,
we can use kwarg whenever we want or we can leave it in function
we can add some char in args kwargs as shown below
"""


# def funargs(normal, *argsname, **kwargsidentity):
#     print(normal)
#
#     for item in argsname:
#         print(item)
#
#     for key, value in kwargsidentity.items():
#         print(f"{key} is a {value}")
#
#
# normal = "Shaikh Nabeel"
# Candidates = ['Nabeel', 'Sameer', 'Aman']
# ability = {"Nabeel": "Programmer", "Sameer": "Astrologer", "Nirbhay": "Programmer"}
# funargs(normal, *Candidates, **ability)

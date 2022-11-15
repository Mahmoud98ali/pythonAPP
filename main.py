# tax = input("Enter Tax: ")
# tax_one= float(tax)/100
# price = input("Enter Price: ")
# sum = float(price) * tax_one
# a =sum +float(price)
# print("Financial tax is: ",a)
# # =========================================
# def say_hi(user="mahmoud"):
#     print("hello "+user)
#
# print("hello 1")
# say_hi()
# print("hello 2")

#
# def cube(num):
#     return num*num*num
#
# result = cube(4)
#
# print(result)

# =============================

# a = 12
# b = 32
# if a > b:
#     print("hello")
# else:
#     print("hi")


# is_hungry = False
# wants_to_eat = True
#
# if is_hungry and wants_to_eat:
#     print("Go eat you are hungry And you want to eat")
# elif is_hungry and not wants_to_eat:
#     print("Eat So you can survive")
# elif not is_hungry and  wants_to_eat:
#     print("do not eat you are not hungry")
# else:
#     print("do not eat")

# ===============================

# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
#
# max_q = max_num(-4343, 12, 232)
# # OR
# print(max(121, 54, 6, 3, 8))

# ===============================
#
# months = {
#     "jan": "january",
#     "feb": "february",
#     "mar": "march"
# }
#
# print(months.get())

# ==============================
#
# i =1
#
# while i<10:
#     print(i)
#     i+=1
# else:
#     print("i is end")
# =================================
# 2D Lists

# no_list = [[1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 3, 5]]
# print(no_list)
#
# for row in no_list:
#     print(row)
#     for column in row:
#         print(column)
# =======================
#
# try:
#     value = int(input("Enter a number: "))
#     print(value)
#     print("Success")
# except ValueError as error:
#     print(error)
#
# ===========================
# # read files
#
# names_file = open("names","r")
# # print(names_file.read())
# # print(names_file.readlines())
# for names in names_file.readlines():
#     print(names)
# names_file.close()

# =============================
# write files
# names_file = open("names","w")
# # names_file.write("<p>this is web</p>")
# list_of_phrases = ["this is a first line","\nthis is a second line","\nthis is a third line"]
# names_file.writelines(list_of_phrases)
# names_file.close()
# =================================
# import docx
# import def_power
#
# print(def_power.power(2,-2))

# =================================
from Employee import Employee
from Employee import Animals

employee1 = Employee("ahmad","male",32,"damascus",4)
employee2 = Employee("ahmad","male",32,"damascus",5)

print(employee1.is_excellent(),employee2.is_excellent())
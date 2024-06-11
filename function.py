# def square(x):
#     return x ** 2

# result = square(13)
# print("THIS FUNCTION IS RETURN AND ARGUMENT TYPE: ")
# print(result)



# def add(numOne, numTwo):
#     return numOne + numTwo

# print("THIS FUNCTION IS RETURN AND ARGUMENT TYPE: ")
# print(add(5, 5))




# def multiply(p1, p2):
#     return p1 * p2

# print(multiply(8, 5))
# print(multiply('a', 5))
# print(multiply(5, 'a'))




# import math

# def circle_stats(radius):
#     area = math.pi * radius ** 2
#     circumference = 2 * math.pi * radius
#     return area, circumference

# x ,y = circle_stats(3)
# print("THIS FUNCTION IS RETURN AND ARGUMENT TYPE: ALSO WE CAN RETURN TWO OR MORE VALUES: ALSO DEPENDS ON THE ORDER OR RETURN")
# print("Area: ", x , "Circumference: ", y)




# def greet(name = "User"):
#     return "Hello, " + name + " !"

# print("IF THE VALUE NOT GIVEN THEN IT WILL USE THE DEFAULT VALUE THAT WE CAN AT THE PARMENTER OF THE FUNCTION SAME AS JAVA SCRIPT")
# print(greet("chai"))
# print(greet())

 
 
 
# cube = lambda x: x ** 3
# print("ANOTHER TYPE OF FUCNTION THAT WE USE :")
# print(cube(3))
 
 


# def sum_all(*args):
#     print(args)
#     for i in args:
#         print(i * 2)
#     return sum(args)

# print(sum_all(1, 2, 3))
# print(sum_all(1, 2, 3, 4, 5))
# print(sum_all(1, 2, 3, 4, 5, 6, 7, 8))




# def print_kwargs(**mma):
#     for fighter, titles in mma.items():
#         print(f"{fighter}: {titles}")

# print("Create a function that accepts any number of keyword arguments and prints them in the format key: value.")
# print_kwargs(name="ALEX PERIERS", titles="TWO DIVISION MMA AND AND TWO DIVISION GLORY")
# print_kwargs(name="JON JONES", titles= "TWO DIVISION MMA ")
# print_kwargs(name="DC", titles="TWO DIVISION ", enemy = "JON JONES")




# def even_generator(limit):
#     for i in range(2, limit + 1, 2):
#         yield i

# for num in even_generator(10):
#     print(num)
    
    
    

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# n = int(input())
# print("FACTORIAL OF NUMBER THAT YOU ENTERED :  " , factorial(n))
    
    
    
    
    
# ++++++++++++++SCOPES++++++++++++++++

    
# username = "this is the global variable same as other language: "

# def func():
#     username = "local variable call only when function will call:"
#     print(username)

# func()
# print(username)




# x = 99 
# def func2(y):
#     z = x + y
#     return z

# result = func2(1)
# print(result)

# def func3():             # this function use to change the value of global variable
#     global x
#     x = 12
    
# func3()
# print(x)




# def f1():               # this is the example of the nested function and calling the main function and task done by the second function
#     x = 88
#     def f2():
#         print(x)
#     return f2
# myResult = f1()
# myResult()




# def chaicoder(num):
#     def actual(x):
#         return x ** num
#     return actual

# f = chaicoder(2)
# g = chaicoder(3)

# print(f(3))
# print(g(3))

# print(chaicoder(5)(2))        # we can call nested  function like this 




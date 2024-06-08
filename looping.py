# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# positive_number_count = 0
# for num in numbers:
#     if num > 0:
#         positive_number_count += 1
# print("Final count of Positive number is: ", positive_number_count)




# n = 10
# sum_even = 0

# for i in range(1, n+1):
#     if i%2 == 0:
#         sum_even += i

# print("Sum of even number is: , ", sum_even)




# x = int(input())
# y = int(input()) 
# sum_even = 0

# for i in range(x, y+1):
#     if i%2 == 0:
#         sum_even += i

# print("Sum of even number is: , ", sum_even)





# number = 3

# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(number, 'x', i, '=', number * i)
    
    
    

# input_str = "Python"
# reversed_str = ""

# for char in input_str:
#     reversed_str = char + reversed_str  

# print(reversed_str)




# input_str = "teeteracdacd"

# for char in input_str:
#     print(char)
#     if input_str.count(char) == 1:
#         print("Char is: ", char)
#         break    
    
    


# number = 5
# factorial = 1

# while number > 0:
#     # factorial = factorial * number
#     # number = number - 1
#     factorial *= number
#     number -= 1

# print("Factorial: ", factorial)




# while True:
#     number = int(input("Enter value b/w 1 and 10: "))
#     if 1 <= number <= 10:
#         print("Thanks")
#         break
#     else:
#         print("Invalid number, try again")
        
        


# number = 28

# is_prime = True

# if number > 1:
#     for i in range(2, number):
#         if (number % i) == 0:
#             is_prime = False
#             break

# print(is_prime)




# items = ["apple", "banana", "orange", "apple", "mango"]

# unique_item = set()

# for item in items:
#     if item in unique_item:
#         print("Duplicate: ", item)
#         break
#     unique_item.add(item)
    
    
    

# import time

# wait_time = 1
# max_retries = 5
# attempts = 0

# while attempts < max_retries:
#     print("Attempt", attempts + 1, "- wait time", wait_time, )
#     time.sleep(wait_time)
#     wait_time *= 2
#     attempts += 1
    
    
    

# import time
# print("chai is here")
# username = "hitesh"
# print(username)
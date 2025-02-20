'''
1. Given an array of integers, write a function to calculate the sum of all elements in the array.

Analyze the time complexity of your solution using Big O notation, especially what is the Big O notation of the code you wrote, and include it in the comments of your program.
'''


import random #used this so that I could have a random array of integers and not a hard coded one.

def sum_of_ints(arr): #funtion to calculate the sum of the integers
    total = 0
    for num in arr:
        total += num
    return total


ints = [random.randint(1, 100) for i in range(10)] #creating a random array of integers
print(ints) #shows the array of integers.
print(sum_of_ints(ints)) #calls the function and prints the sum of the array.

#this function is O(n) because there is only one for loop that it iterates through once
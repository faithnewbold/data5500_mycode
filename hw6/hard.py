'''
3. Write a function that takes an array of integers as input and returns the maximum difference between any two numbers in the array.

Analyze the time complexity of your solution using Big O notation, especially what is the Big O notation of the code you wrote, and include it in the comments of your program.
'''

import random #used this so that I could have a random array of integers and not a hard coded one.

def max_and_min(arr):
    max_num = 0 #initializing both variables
    min_num = 100
    
    for num in arr:
        if num > max_num: 
            max_num = num #setting the max_num to the greatest variable
        if num < min_num:
            min_num = num #setting the min_num to the lowest variable

    return max_num - min_num #finding the difference


ints = [random.randint(1, 100) for i in range(10)] #creating a random array of integers
print(ints) #shows the array of integers.
print(max_and_min(ints))

#this would also be O(n) because there is only one for loop that it is looping through once.
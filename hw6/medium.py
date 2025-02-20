'''
2. Given an array of integers, write a function that finds the second largest number in the array.

Analyze the time complexity of your solution using Big O notation, especially what is the Big O notation of the code you wrote, and include it in the comments of your program.
'''

import random #used this so that I could have a random array of integers and not a hard coded one.

def second_largest(arr):
    largest = 0 #creating largest and second largest variables
    second = 0
    for num in arr:
        if num > largest:
            second = largest #make second value of largest if a number is found that is higher
            largest = num #make largest the highest value
        elif largest > num > second:
            second = num

    return second


ints = [random.randint(1, 100) for i in range(10)] #creating a random array of integers
print(ints) #shows the array of integers.
print(second_largest(ints))

#this is O(n) since there is only one for loop that it has to iterate through once.
# examping 1 - printing numbers
# Printing numbers iterative
nums = [3, 1, 4, 1, 5, 9, 2, 6]

for i in range(len(nums)):
    print(nums[i], end = " ")
print()

# Printing numbers recursively, this means it is a function that calls itself
def print_nums(nums, i):
    if i >= len(nums):
        return
    
    print(nums[i], end = " ")
    print_nums(nums, i+1)
    
print_nums(nums, 0)


#example 2 - summing up numbers
#sum up numbers iteratively
def sum_numbers(n):
    total = 0
    for i in range(n+1):
        total += i
    print(total)
    return total

print("iterative 100:", sum_numbers(100))

#now sum up numbers recursively
def sum_number_rec(n):
    if n == 1: #X/\ (shut it down)
        return n #recursive call

    #the logic
    return sum_number_rec(n-1) + n # 1 + 2 + 3 + 4 + ... + 99 + 100

print("recursion 100:", sum_number_rec(100))


#example 3 - factorials
#factorial iteratively
def factorial(n):
    tot = 1
    for i in range(1, n+1):
        tot *= i
    return tot

print("Iterative factorial:", factorial(5)) #should give 120

#factorial recursively - factorials are recursive by nature!!!!
# it is recursive because factorial 10 is the same as factorial 10*factorial 9
def factorial_rec(n):
    if n == 2: #X/\
        return n

    return n * factorial_rec(n-1)

print("recursion factorial:", factorial_rec(5)) #should again be 120


#example 4 - fibanocci series - much easier to solve with recursion
#means every number in the series is the sum of the previous two numbers - it uses recursion because it takes the numbers before it
def fib(n):
    if n == 0: #there are not fib rules with the 0 and 1, they are by rule 0 and 1 = X/\
        return 0
    if n == 1:
        return 1

    return fib(n-1) + fib(n-2)

print(fib(11)) #should give 89 for the 11th term

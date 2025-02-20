# lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9]
import random


#write an algorithm that sorts that data (that doesn't use .sort())

for i in range(len(lst)-1):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            (lst[i], lst[i+1]) = (lst[i+1], lst[i])

print(lst)

#then make it faster
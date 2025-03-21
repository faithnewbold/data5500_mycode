
lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9]
# import random


#write an algorithm that sorts that data (that doesn't use .sort())

for i in range(len(lst)-1):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            (lst[i], lst[i+1]) = (lst[i+1], lst[i])

print("Bubble Sort:", lst)

#then make it faster

#selection sort - you select the smallest and you swap it
lst2 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9]

for i in range(len(lst2)):

    min_inx = i
    for j in range(i+1, len(lst2)):
        if lst2[min_inx] > lst2[j]:
            min_inx = j

    lst2[i], lst2[min_inx] = lst2[min_inx], lst2[i]

print("Selection Sort:", lst2)

#insertion sort - split up list into 2 lists
lst3 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9]

for i in range(1, len(lst3)):
    key = lst3[i]

    j = i-1
    while j>=0 and key < lst3[j]:
        j -= 1

    lst3[j+1] = key

print("Insertion Sort:", lst3)

#merge sort - all about buckets - merge buckets and sort them as you are merging
def merge(arr, l, m, r):
    n1 = m-l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m+1+j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
  
    # Copy the remaining elements of L[], if there 
    # are any 
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    # Copy the remaining elements of R[], if there 
    # are any 
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
  
# l is for left index and r is right index of the 
# sub-array of arr to be sorted 
def mergeSort(arr,l,r): 
    if l < r: 
  
        # Same as (l+r)//2, but avoids overflow for 
        # large l and h 
        m = (l+(r-1))//2
  
        # Sort first and second halves 
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r) 
  
  
# Driver code to test above 
arr = [3, 1, 4, 1, 5, 9, 2, 6] 
print("unsorted array:", arr)
mergeSort(arr,0,len(arr)-1) 
print("merge sort:", arr)


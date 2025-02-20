for i in range(1000): #this is order n / O(n)
    print(i)

for i in range(1000): #this is O(n squared) because it is nested
    for j in range(1000):
        print(i, j) #this ran 1 million times - took 14 seconds to run

for i in range(1000): #this is O(n cubed) because it has two nested inside
    for j in range(1000):
        for k in range(1000):
            print(i,j,k) #this runs 1 billion times - this will take about 4 hours to run

for l in range(1000):
    for k in range(1000):
        for i in range(1000):
            for j in range(1000):
                print(l,k,i,j) #this would take 162 days to run
                #if i add another, it'll take 162000 days, which is 443 years

#what we have to do is parallelize it and bring it down to be two o(n squared) instead of an o(n to the fifth)

#however, it should be in terms of n
list_n = [i for i in range(1000)]

for i in list_n:
    for j in list_n:
        print(i,j)
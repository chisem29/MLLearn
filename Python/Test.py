from random import randint
from time import time

def quick(l) :
    if len(l) == 0 :
        return l
    m = l[len(l) // 2]
    mid = [i for i in l if m == i]
    left = [i for i in l if m > i]
    right = [i for i in l if m < i]
    return quick(left) + mid + quick(right)

def bubble(l) :
    ll = len(l)
    for i in range(ll - 1) :
        for j in range(i+1, ll) :
            if l[i] > l[j] :
                l[j], l[i] = l[i], l[j]
    return l

arr = [randint(1, 100) for i in range(10000)]

sq = time()

print("quick", quick(arr))
print(time() - sq)

sb = time() 

print("bubble", bubble(arr))
print(time() - sb)
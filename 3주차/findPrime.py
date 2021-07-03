import sys,re
from collections import deque
from itertools import permutations,combinations


def find_prime(n):
    if n==1: return False
    for i in range(2,n):
        if (n % i == 0):
            return False
    return True

def make_num(lst):
    s=0
    for i in range(len(lst)):
        s= s + int(lst[len(lst)-i-1]) * (10**i)
    return s

if __name__=='__main__':
    num_str= input()
    nums = list()


    for i in range(len(num_str)):
        per=  list(permutations(num_str,i+1))
        sum=0
        for j in range(len(per)):
            nums.append(make_num(per[j]))


    ansList= deque()

    for i in range(len(nums)):
        if find_prime(nums[i])== True:
            if nums[i] not in ansList: ansList.append(nums[i])
        else: None

    print(len(ansList))

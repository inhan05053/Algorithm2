
import sys
n,k = list(map(int, sys.stdin.readline().split(" ")))
time =(list(map(int,sys.stdin.readline().split(" "))))
result = 0
left = min(time)
right= min(time)*k

while True:
    mid = (left+right) // 2
    sumMidDivTime =0
    for i in range(n):
        sumMidDivTime += mid//time[i]
    if sumMidDivTime < k:
        left= mid +1
    else:
        result = mid
        right = mid-1

    if left >right:
        break

print(result)
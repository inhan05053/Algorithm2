
import sys
value=[]
calorie=[]

n,k = list(map(float, sys.stdin.readline().split(" ")))
n= int(n)
k=k*100
for i in range(n):
    cal,val =list(map(float, sys.stdin.readline().split(" ")))
    value.append(val)
    cal = int(cal)
    calorie.append(cal*100)

twod_list= [[0 for x in range(int(k)+1)] for y in range(n+1)]

for i in range(1,n+1):
    for j in range(1,int(k)+1):
        if calorie[i-1] > j:
            twod_list[i][j] = twod_list[i-1][j]
        else:
            twod_list[i][j] = max(value[i-1] + twod_list[i][j-calorie[i-1]], twod_list[i-1][j])
print(int((twod_list[n][int(k)])))

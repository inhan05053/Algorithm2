
import sys
import numpy as np
maxNum= 1000000001
m ,n = list(map(int, sys.stdin.readline().split(" ")))
array=np.zeros((m,n), int)
result=np.zeros((m,n), int)

for i in range(m):
    array[i,:]=(list(map(int, sys.stdin.readline().split(" "))))
num=1
renum=0

while renum<n*m: #n*m 의 결과 list에 모든 값을 다 채워주면 종료
    maxList=[]
    for i in range(n):
        array2= array[:,i]
        minValue= min(array2) #행 중에서 가장 작은 값 찾는 과정
        cnt= array2.tolist().count(minValue) #가장 작은 값의 개수
        j= array2.tolist().index(minValue)  # 행중에서 가장 작은 값의 개수
        if minValue == min(array[j,:]) and minValue != 1000000001: #행에서 가장 작은 값이 열에서도 가장 작다면 결과 list에 추가
            result[j,i]=num
            maxList.append((j,i))
            renum+=1
        if cnt>=2:
            while cnt>1:  # 동일한 값을 처리해 주기 위한 코드  (위의 while문과 동일)
                array2 = array[j+1:,i]
                minValue = min(array2)
                cnt = array2.tolist().count(minValue)
                j = array2.tolist().index(minValue)+j+1
                if minValue == min(array[j,:]) and minValue != 1000000001 :
                    result[j,i] = num
                    maxList.append((j, i))
                    renum+=1
                cnt-1

    for k in range(len(maxList)): # 결과 list에 들어간 인덱스의 값을 1000000001로 채운다.
        array[maxList[k][0],maxList[k][1]]= maxNum
    num+=1


for i in result: #2차원 List를 출력하기위한 포맷
    for j in i:
        print(j, end=' ')
    print()
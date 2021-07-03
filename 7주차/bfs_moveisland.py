import sys
from copy import deepcopy
sys.setrecursionlimit(10**6)

dx= [-1, 1, 0, 0]
dy= [0, 0, -1, 1]
n= int(input())
array=[]  # 지도를 입력 받을 LIST
array2=[] # array와 비슷한 모습이지만 1이 아닌 음수 값으로 섬의 번호를 명명
islandBoundary=[] # 바다와 섬의 경계선
newBoundary=[] # 섬의 확장에 따른 새로운 경계선
numOfIsland=[] # 섬의 번호 모음
for _ in range(n):
    array.append(list(map(int, input().split(" "))))

for _ in range(n):
    array2.append(list(map(int, "0"*n)))




def groupOfIsland(i, j, parentNumber):  #섬을 그룹핑 해주는 함수. 섬의 이름을 음수 값으로 설정
    if array2[i][j] < 0:
        return
    array2[i][j] = parentNumber
    numOfIsland.append(parentNumber)
    islandBoundary.append((i,j,parentNumber))
    for k in range(4):
        if n >i+dx[k] >= 0  and n > j+dy[k] >=0:
            if array[i+dx[k]][j+dy[k]] ==0 :
                islandBoundary.append((i,j,parentNumber))
            if array[i+dx[k]][j+dy[k]]<=0 : continue
            groupOfIsland(i + dx[k], j + dy[k], parentNumber)  #재귀를 이용해 같은 섬을 찾는 과정

def expandIsland(boundary,array_island):  #섬을 한칸씩 확장해나가는 함수
    global count
    count=0
    array_ = deepcopy(array_island) #깊은 복사를 이용해 섬의 모습을 유지
    while(1):
        lenboundary=len(boundary)
        count += 1
        for q in range(lenboundary):
            a=boundary[q][0]  # 위치 X 좌표
            b=boundary[q][1 ] # 위치 Y 좌표
            c=boundary[q][2]  # 섬의 번호(음수값)

            for k in range(4):  # 상하좌우 확장할 수 있는지 여부를 따지는 과정
                if n >a+dx[k] >= 0  and n > b+dy[k] >=0:
                    if array_[a + dx[k]][b + dy[k]] == c: continue
                    elif array_[a + dx[k]][b + dy[k]] < 0:
                        newBoundary.clear()
                        return
                    array_[a + dx[k]][b + dy[k]] = c
                    newBoundary.append((a + dx[k],b + dy[k],c))

        boundary=newBoundary[:]
        newBoundary.clear()


for i in range(n):
    for j in range(n):
        if array[i][j] > 0:
            groupOfIsland(i, j, -(10 * i + j)-1)  #섬들을 그룹핑해주는 작업

numOfIsland=sorted(numOfIsland)  #섬의 번호를 정렬
islandBoundary= list(set(islandBoundary))
islandBoundary= sorted(islandBoundary, key = lambda x:x[2]) #섬의 위치와 번호를 번호 순서대로 정렬
precount=500
prevent_numc=0
sum=0
while(1):
    num_c=numOfIsland.count(numOfIsland[sum])
    sum=sum+num_c
    expandIsland(islandBoundary[prevent_numc:sum],array2)
    count=min(precount,count)  #가장 짧은 거리의 섬으로 최신화
    prevent_numc=sum
    precount=count
    if sum != len(islandBoundary):
        continue
    break
print(count-1)

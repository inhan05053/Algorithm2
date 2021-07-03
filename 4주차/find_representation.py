import sys


if __name__=='__main__':
    num = int(sys.stdin.readline())
    rank = list([[0 for col in range(2)] for row in range(num)])

    for i in range(num):   #반복을 통해 각각의 등수를 리스트에 담는다
        fst,snd = list(map(int, sys.stdin.readline().split(" ")))
        rank[fst-1][0]= fst
        rank[fst-1][1]= snd

    result=0  #대표선수의 수
    min_rank=num+1  #첫과목이 자신보다 높은 사람중 두번째 등수가 가장 높은 등수

    for i in range(num):  #두번째 과목이 min_rank보다 작다면 result+=1
        if rank[i][1]<min_rank:
            min_rank=rank[i][1]  #두번째 과목이 더 높은 사람이 들어왔으므로 등수를 최신화
            result+=1

    print(result)
import sys


if __name__=='__main__':
    num = int(sys.stdin.readline())
    eat = int(sys.stdin.readline())
    move = int(sys.stdin.readline())

    eat_area=list()
    move_dic =list()

    dx=[0,-1,0,1]  #L,U,R,D 순서
    dy=[-1,0,1,0]

    for i in range(eat):
        n,m= list(map(int,input().split()))
        eat_area.append([n,m])

    for i in range(move):
        n, m = list(map(str, input().split()))
        move_dic.append([int(n),m])


    x,y=1,1 #현재 지렁이의 위치 x,y
    result=0 # output 값
    route=list() # 현재 지렁이가 밟고있는 경로
    route.append([1,1]) #시작점은 밟고 있다고 가정
    state = 2 # 현재 오른쪽 방향으로 진행중


    while True:
        if move_dic:
            count,dic = move_dic[0]

        if count == result:
            move_dic.pop(0)
            if dic == 'R':  # R이므로 우회전하게 된다.
                x= x+dx[(state+1)%4]   # x값을 최신화 dx 만큼 이동
                y= y+dy[(state+1)%4]   #  위와 동일
                state = (state +1)%4   # (state+1)%4 진행방향을 바꾸는 코드
            elif dic== 'L':  # L이므로 좌회전하게 된다.
                x = x + dx[(state+3)%4]
                y = y + dy[(state+3)%4]
                state = (state -1)%4
        else :  # 현재의 방향으로 계속 진행
            x = x+ dx[state]
            y = y+ dy[state]

        result +=1  #이동 수에 1을 더한다.

        #종료조건 검사
        if x<1 or x>num or y<1 or y>num or [x,y] in route:
            break

        # 먹이를 먹지 못했으면 새로운 위치를 추가하고 꼬리부분 위치를 삭제
        # 먹이를 먹었다면 새로운 위치만 추가
        if [x,y] not in eat_area:
            route.pop(0)
        route.append([x,y])

    print(result)




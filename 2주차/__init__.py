import sys

lst_ans = []
num_str= int(sys.stdin.readline())
for i in range(num_str):
    only_ab = list(map(str, sys.stdin.readline()))
    only_ab.pop()
    sum = 0
    continu_a= 0
    for j in range (len(only_ab)) :
        if 'A' == only_ab[j]:
            continu_a+=1
            sum += continu_a
        else :
            continu_a = 0
    lst_ans.append(sum)
for i in range(len(lst_ans)) :
    print(lst_ans[i])

array=[]
n= int(input())
array= list(map(str, input().split(" ")))
array2= list(map(len,array))
array3=[]
for i in range(len(array)):
    array3.append([array[i],array2[i]]) #array3에는 str형 숫자와 숫자의 길이(자리수)를 저장

def sort_desc(lst):  #내림차순으로 정렬하기 위한 코드
    copy_lst= lst[:]
    for i in range(len(copy_lst)):  #숫자의 길이를 최대 길이로 모두 맞춰준다.
        maxLength =max(array2)
        multiValue = int(maxLength / array2[i])
        copy_lst[i][0]= str(copy_lst[i][0]) * multiValue

    copy_lst = sorted(copy_lst)  #길이가 맞춰준 숫자를 크기별로 정렬한다.

    for i in range(len(copy_lst)):  #일정했던 숫자들을 다시 원래 상태로 되돌린다.
        copy_lst[i][0]=  copy_lst[i][0][:copy_lst[i][1]]

    copy_lst.reverse() #내림차순으로 하기 위해 reverse해준다.

    return copy_lst

def paste_number(array):  #내림차순으로 정렬된 숫자들을 연결해주는 작업
    result=''
    for i in range(len(array)):
        result =result + array[i][0]
    return result

array_desc=sort_desc(array3)  #숫자들을 합쳤을때 제일 크게되도록 정렬

rult= paste_number(array_desc)  #정렬된 숫자들을 연결

print(int(rult))
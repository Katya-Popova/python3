#Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
n = int(input())
some_list=[]
num=-1
num2=1
for i in range(n):
    if i<2:
        some_list.append(num)
    elif i>1:
        num=some_list[i-1]+some_list[i-2]
        some_list.append(num)

new_list=[]
for j in range(n):
    if j<2:
        new_list.append(num2)
    elif j>1:
        num2=new_list[j-1]+new_list[j-2]
        new_list.append(num2)

some_list1=some_list[::-1]
some_list1.append(0)
next_list=some_list1+new_list
print(next_list)

#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
n=int(input())
some_list=[]
while n>0:
    some_list.append(n%2)
    n=n//2
new_list=some_list[::-1]
print(new_list)
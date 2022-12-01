#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
some_list=[2,3,5,6]
count=0
n=len(some_list)
x=int(n/2)
if n%2==0:
    for i in range(0,x):
        count=int(some_list[i])*int(some_list[n-1])
        n=n-1
        print(count)
else:
    for i in range(0,x):
        count=int(some_list[i])*int(some_list[n-1])
        n=n-1
        print(count)
    print(some_list[x]*some_list[x])
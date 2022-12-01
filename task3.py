#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементо
some_list=[1.1, 1.2, 3.1, 5, 10.01]
n=len(some_list)
new_list=[]
for i in range(n):
    some_list[i]=round((some_list[i]-int(some_list[i])),2)
    if some_list[i] !=0:
       new_list.append(some_list[i])
print(max(new_list)-min(new_list))    


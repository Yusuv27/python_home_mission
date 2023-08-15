#1 задание
first_number=int(input("Введите первое число: "))
difference=int(input("Введите разницу: "))
end_number=int(input("Введите конечное число: "))
list_1=[]
for i in range(0,end_number):
    list_1.append(first_number)
    first_number=first_number+difference
print(list_1)

#2 задание
list_2= input("Введите строку: ").split()
min=int(input("Введите минимальное значение: "))
max=int(input("Введите максимальное значение: "))
list_3=[]
y=0
for i in list_2:
    x=int(i)
    if x >= min and x <= max:
        list_3.append(y)
    y+=1
print(list_3)
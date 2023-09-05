# list_1=[1,2,3,5,8,15,23,38]
# list_2=[]
# def chetno(list_1):
#     for i in range(0,len(list_1)):
#         if list_1[i]%2==0:
#             list_2.append((list_1[i],list_1[i]*list_1[i]))
#     print(list_2)
# chetno(list_1)

# def select(f,col):
#     return[f(x) for x in col]

# def where(f,col):
#     return[x for x in col if f(x)]

# data=[1,2,3,5,8,15,23,38]
# res=select(int,data)
# print(res)
# res=where(lambda x:x%2==0,res)
# print(res)
# res=list(select (lambda x: (x,x**2),res))
# print(res)

# list_1 = [x for x in range (1,20)]
# print(list_1)

# list_1=list(map(lambda x:x+10,list_1))
# print(list_1)

# data = ' 15 156 96 3 5 8 52 5'
# print(data)
# data=list(map(int,data.split()))
# print(data)

# data = [15,65,9,36,175]
# res = list(filter(lambda x: x % 10 == 5,data))
# print(res)

# colors = ['red','g555','blue']
# data = open ('file.txt','a')
# data.writelines(colors)
# data.close()

with open('file.txt','w') as data:
    data.write ('line 1\n')
    data.write('line 2\n')
    a=0
    for i in range(0,100000):
        data.writelines(str(a)+" ")
        a+=12

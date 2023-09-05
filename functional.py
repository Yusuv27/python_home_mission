def Phone():
    with open('number_phone.txt','a') as data:
        surname=(str(input("Введите фамилию: ")))
        name=(str(input("Введите имя: ")))
        name_father=(str(input("Введите отчество: ")))
        number_phone=(str(input("Введите номер: ")))
        data.write(f'{surname} {name} {name_father} {number_phone}\n')
        data.close()
# Phone()
def Phone_check():
    with open('number_phone.txt','r') as data:
        for line in data:
            print(line)
        data.close()
def Phone_fade():
    name_1=input("Введите фамилию: ")
    with open('number_phone.txt','r') as data:
        for line in data:
            line=line.split()
            if name_1 in line[0]:
                result=' '.join(line)
                print(result)
                data.close()
                return
        print("Такого человека нет")
    data.close()
# Phone_fade()

def Phone_fade_2():
    name_1=input("Введите фамилию: ")
    with open('number_phone.txt','r+') as data:
        for line in data:
            line=line.split()
            if name_1 in line[0]:
                line_delete_1=line[0]
                line[0]=input("Введите фамилию для изменения: ")
                result=' '.join(line)
                print(result)
                # data.write(str(result)+"\n")
                data.close()
                with open ('number_phone.txt', 'r') as data:
                    old_data = data.read()
                    new_data = old_data.replace(line_delete_1,line[0])
                data.close()
                with open ('number_phone.txt', 'w') as data:
                    data.write(new_data)
                data.close()
                return 
        print("Такого человека нет")
    data.close()
# Phone_fade_2()
def Phone_fade_3():
    name_1=input("Введите фамилию: ")
    with open('number_phone.txt','r') as data:
        for line in data:
            line=line.split()
            if name_1 in line[1]:
                result=' '.join(line)
                print(result)
                data.close()
                return
        print("Такого человека нет")
    data.close()
# Phone_fade_3():
def Phone_fade_4():
    name_1=input("Введите фамилию: ")
    with open('number_phone.txt','r+') as data:
        for line in data:
            line=line.split()
            if name_1 in line[0]:
                line_delete_1=line[1]
                line[1]=input("Введите имя для изменения: ")
                result=' '.join(line)
                print(result)
                data.close()
                with open ('number_phone.txt', 'r') as data:
                    old_data = data.read()
                    new_data = old_data.replace(line_delete_1,line[1])
                data.close()
                with open ('number_phone.txt', 'w') as data:
                    data.write(new_data)
                data.close()
                return 
        print("Такого человека нет")
    data.close()
# Phone_fade_4()

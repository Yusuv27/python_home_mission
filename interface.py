import functional
def menu_1():
    menu=int(input(" 1 - Посмотреть список \n 2 - Найти номер по фамилии \n 3 - Изменить фамилию\n 4 - Добавить контакт \n Введите число:\n"))
    if menu == 1:
        functional.Phone_check()
    elif menu == 2:
        functional.Phone_fade()
    elif menu == 3:
        functional.Phone_fade_2()
    elif menu == 4:
        functional.Phone()
    else:
        print("Неверно введены данные")
    menu_3=int(input(" 1 - Да \n 2 - Нет \n Желаете продолжить работу с программой?\n"))
    if menu_3==1:
        menu_1()
    elif menu_3==2:
        return
    else:
        print("Неверно введены данные")
menu_1()
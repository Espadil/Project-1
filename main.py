# MyProfile app

SEPARATOR = '------------------------------------------'

# user profile
n = ''
a = 0
ph = ''
e = ''
i = ''
in_adres = ''
adres = ''
# social links
OGRNIP = ''
INN = ''
bank = ''


def general_info_user(n_parameter, a_parameter, ph_parameter, e_parameter, i_parameter, in_adres_parameter,
                      adres_parameter):
    print(SEPARATOR)
    print('Имя:    ', n_parameter)
    if 11 <= a_parameter % 100 <= 19:
        years_parameter = 'лет'
    elif a_parameter % 10 == 1:
        years_parameter = 'год'
    elif 2 <= a_parameter % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'

    print('Возраст:', a_parameter, years_parameter)
    print('Телефон:', ph_parameter)
    print('E-mail: ', e_parameter)
    print('Почтовый идекс: ', in_adres_parameter)
    print('Адрес: ', adres_parameter)
    if i:
        print('')
        print('Дополнительная информация:')
        print(i_parameter)


#print('Приложение MyProfile')
#print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        break

    if option == 1:
        # submenu 1: edit info
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # input general info
                n = input('Введите имя: ')
                while 1:
                    # validate user age
                    a = int(input('Введите возраст: '))
                    if a > 0:
                        break
                    print('Возраст должен быть положительным')

                uph = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                ph = ''
                for ch in uph:
                    if ch == '+' or ('0' <= ch <= '9'):
                        ph += ch

                e = input('Введите адрес электронной почты: ')
                in_adres_1 = input('Введите почтовый индекс: ')
                in_adres = "".join(c for c in in_adres_1 if c.isdecimal())
                adres = input('Введите ваш адрес: ')
                i = input('Введите дополнительную информацию:\n')

            elif option2 == 2:
                # input social links
                while 1:
                    OGRNIP = input('Введите ОГРНИП: ')
                    if len(OGRNIP) == 15:
                        break
                    print('ОГРНИП должен содержать 15 цифр.')
                INN = input('Введите ИНН: ')
                while 1:
                    bank = input('Введите банковский счёт: ')
                    if len(bank) == 20:
                        break
                    print('Банковский счёт должен содержать 20 цифр.')
            else:
                print('Введите корректный пункт меню')
    elif option == 2:
        # submenu 2: print info
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                general_info_user(n, a, ph, e, i, in_adres, adres)

            elif option2 == 2:
                general_info_user(n, a, ph, e, i, in_adres, adres)

                # print social links
                print('')
                print('Информация о предпринимателе')
                print('ОГРНИП:', OGRNIP)
                print('ИНН: ', INN)
                print('Банковский счёт: ', bank)
            else:
                print('Введите корректный пункт меню')
    else:
        print('Введите корректный пункт меню')
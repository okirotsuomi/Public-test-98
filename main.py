price_all = 0
while True:
    try:
        ticket_num = int(input('Сколько билетов вы хотите приобрести на мероприятие: '))
        if type(ticket_num) == int:
            break
    except ValueError:
        print('Введите целое число')
for i in range(ticket_num):
    i = i + 1
    while True:
        try:
            age = int(input(f'Возраст поситителя по билету №{i}: '))
            if age < 18:
                print('Вы проходите бесплатно')
            elif age >= 18 and age <25:
                price_all += 990
                print('Стоимость билета - 990 руб.')
            else:
                price_all += 1390
                print('Стоимость билета - 1390 руб.')
            if type(age) == int:
                break
        except ValueError:
            print('Введите целое число')
if ticket_num > 3:
    price_all = price_all - ((price_all/100)*10)
    print('Скидка на полную стоимость билетов за регистрацию более трёх человек - 10%')
    print(f'Сумма к оплате {price_all} руб.')
else:
    print(f'Сумма к оплате {price_all} руб.')
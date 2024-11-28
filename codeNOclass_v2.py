print('Здравствуйте! Вашему вниманию представленя игра "Симулятор лабораторной работы по ПЦР-анализу".')
print('Выберите уровень: ')
print('1. Подготовительный: легкие теоретические вопросы тествового типа (допускается 3 ошибки).')
print('2. Задачи: начальный уровень, решение задач на концентрации (допускается 3 ошибки).')
print('3. ПЦР: схематическое выполнение анализа (повышенный уровень сложности – ошибки недопустимы).')
current_level = int(input('Введите цифру от 1 до 3, чтобы выбрать уровень: '))
levels = [1, 2, 3]
mist = 0
bag = []
ans_1 = ['а', 'в', 'а', 'г', 'б', 'а', 'б', 'в', 'а', 'г', 'д', 'а', 'а', 'в', 'г', 'г', 'в', 'а', 'б', 'а', 'б', 'а']
ans_2 = ['23,4', '0,68', '3,41', '220,575', '291,62', '4,72', '2,25', '6,25', '20', '1,3611', '3,01', '3,5']
per_ans_1 = [] #список ответов пользователя 1 ур
per_ans_2 = [] #список ответов пользователя 2 ур

if current_level == 1:
    print('Вы выбрали подготовительный уровень!')
    while True:  # бесконечный цикл, который будет прерываться при правильных ответах
        mist = 0
        per_ans_1.clear()  # очищаем список ответов перед новым прохождением
        with open('test_1.txt', 'r', encoding='utf-8') as f1:  # вопросы
            lines = f1.readlines()
        
        for counter_1 in range(len(lines)):
            print(lines[counter_1].strip())  # выводим вопрос
            per_ans = input(('Введите ответ (одна буква): '))  # ответ
            
            if per_ans != ans_1[counter_1]:
                mist += 1  # увеличиваем счетчик ошибок
                print(f'''
                      Присутствует ошибка! Продолжайте решать тест, а пока вот подсказка, вспомните о ней, когда будете перерешивать тест: ''')  # сообщаем об ошибке
                
                # Выводим подсказку
                with open('answer_451.txt', 'r', encoding='utf-8') as help_words:  # подсказки
                    helps = help_words.readlines()
                    print(helps[counter_1])
                
                if mist >= 3:  # если количество ошибок превышает 3
                    print('Превышено допустимое количество ошибок, пожалуйста, начните заново!')
                    break  # выходим из цикла вопросов
            
            per_ans_1.append(per_ans)  # добавляем ответ пользователя в список

        if per_ans_1 == ans_1:  # если все ответы правильные
            print('Отлично! Тест пройден!')
            bag = ['буфер', 'DNTP', 'SYBR', 'праймер', 'полимераза', 'ДНК', 'вода']
            cont_ans = input('Хотите проверить себя на более сложном уровне? (Напишите ответ в формате "Да" или "Нет"(без кавычек)): ')
            if cont_ans.lower() == 'да':
                current_level = int(input('Следующий уровень – решение задач, Вы готовы? Если да, введите цифру 2: '))  # переход на следующий уровень
                break
            else:
                print('Хорошая работа! Отдохните!')
                break
        else:
            print('Стоит попробовать еще раз, где-то есть ошибка!')

if current_level == 2:
    # переход на второй уровень
    print('Вы выбрали уровень 2 – решение задач')
    while current_level == 2:  # прохождение уровня до тех пор, пока не решит правильно или не поменяет уровень
        per_ans_2.clear()  # очищаем список ответов перед новым прохождением
        counter_2 = 0  # сбрасываем счетчик вопросов
        with open('test_2.txt', 'r', encoding='utf-8') as f2:  # задачи
            lines = f2.readlines()
            for line in lines:
                print(line)
                mist_2 = 0  # счетчик попыток
                while mist_2 < 3:  # три попытки на ответ
                    per_ans = input('Введите ответ: ')  # ответ
                    if per_ans == ans_2[counter_2]:
                        per_ans_2.append(per_ans)  # добавляем правильный ответ в список
                        break  # выходим из цикла попыток
                    else:
                        print('Присутствует ошибка!')  # сообщаем об ошибке
                        mist_2 += 1  # увеличиваем счетчик попыток
                        if mist_2 < 3:  # если еще есть попытки
                            with open('help_w_2.txt', 'r', encoding='utf-8') as help_words:  # подсказки
                                helps = help_words.readlines()
                                print(helps[counter_2])  # выводим подсказку для текущего вопроса
                if mist_2 >= 3:  # если исчерпаны все попытки
                    print('Превышено допустимое количество ошибок. Тест завершен.')
                    break  # выходим из цикла вопросов
                counter_2 += 1  # увеличиваем счетчик для следующего вопроса

            if mist_2 < 3 and per_ans_2 == ans_2:  # если все ответы правильные
                print('Отлично! Задачи прорешены! Попробуйте уровень сложнее! Вы получили необходимые материалы для него!')
                bag = ['буфер', 'DNTP', 'SYBR', 'праймер', 'полимераза', 'ДНК', 'вода']
                cont_ans = input('Хотите проверить себя на более сложном уровне? (Напишите ответ в формате "Да" или "Нет"(без кавычек)): ')
                if cont_ans.lower() == 'да':
                    current_level = int(input('Следующий уровень – проведение ПЦР, Вы готовы? Если да, введите цифру 3: '))
                    break
                else:
                    print('Хорошая работа! Отдохните!')
                    break
            elif mist_2 < 3:  # если тест завершен, но не все ответы правильные
                print('Тест завершен, где-то есть ошибка!')

if current_level == 3 and len(bag) > 0:
    # Уровень 3. ПЦР.
    print('Уровень 3: Полимеразная цепная реакция\nПолимеразная цепная реакция – это метод амплификациии определенных фрагментов нуклеиновых кислот in vitro, с помощью которого можно получать большие количества ДНК, необходимые для различных экспериментов и процедур в разных областях.')
    print('Этап 1. Правильная концентрация.\nВам необходимо правильно рассчитать количество микролитров каждого реагента, которое необходимо добавить для проведения реакции (это количество на одну пробу). Вам даны названия реагентов, их начальная и конечная концентрации.\nПомните, что расчет объема воды производится в последнюю очередь. При необходимости получающиеся числовые значения округляйте до десятых.\nПоочередно вводите свои ответы в формате “вещество число” (пример: буфер 0,1).')
    # здесь таблица вещество-Нконц-Кконц
    print(f'{"Вещ-ва":<10}|{"Н.конц.":^9}|{"К.конц.":^9}')
    print(f'{"Буфер":<10}|{"10x":^9}|{"1x":^9}')
    print(f'{"DNTP":<10}|{"2,5":^9}|{"0,25":^9}')
    print(f'{"SYBR":<10}|{"50x":^9}|{"1x":^9}')
    print(f'{"Праймер":<10}|{"3":^9}|{"0,3":^9}')
    print(f'{"Полимераза":<10}|{"5у":^9}|{"0,1у":^9}')
    print(f'"Объем ДНК = 2 мкл"\n"Итоговый объем = 20 мкл"\n"Объем воды = ? мкл"')

    ans3_1 = ['буфер 2', 'dntp 2', 'sybr 0,4', 'праймер 2', 'полимераза 0,4', 'вода 11,2']
    user_ans3_1 = []  # ответы пользователя

    while True:  # Цикл для повторного ввода в случае ошибки
        user_ans3_1.clear()  # Очистка предыдущих ответов
        for i in range(6):  # ввод и проверка ответов
            ua31 = input().lower()
            user_ans3_1.append(ua31)

        if user_ans3_1 == ans3_1:
            print('Отлично, продолжим!')
            break  # Выход из цикла, если ответы верные
        else:
            print('Присутствуют ошибки, перепроверьте и попробуйте еще раз!')

    print('Этап 2. Подготовка пробы.\nТеперь поочередно добавляйте нужное количество каждого реагента в пробирку из расчета "нужное количество проб" + "одна запасная проба".')
    ans3_2 = ['буфер 4', 'dntp 4', 'sybr 0,8', 'праймер 4', 'праймер 4', 'вода 22,4']
    user_ans3_2 = []  # ответы пользователя

    while True:  # Цикл для повторного ввода в случае ошибки
        user_ans3_2.clear()  # Очистка предыдущих ответов
        for i in range(6):  # ввод и проверка ответов
            ua32 = input().lower()
            user_ans3_2.append(ua32)

        if user_ans3_2 == ans3_2:
            print('Отлично, продолжим!')
            break  # Выход из цикла, если ответы верные
        else:
            print('Присутствуют ошибки, перепроверьте и попробуйте еще раз!')

    while True:  # Цикл для повторного ввода в случае ошибки
        ans322 = input('В пробирку с ДНК добавьте необходимое количество смеси: ')
        if ans322 == '18':
            print('Отлично, продолжим!')
            break  # Выход из цикла, если ответ верный
        else:
            print('Присутствуют ошибки, перепроверьте и попробуйте еще раз!')

    print('Этап 3. Амплификация.\nПеред выполнением следующего задания внимательно прочтите текст:\n\nОсновные этапы ПЦР — денатурация, отжиг, элонгация. Начальную стадию денатурации проводят при 94—98 °C в течение 0,5—5 мин. Продолжительность и температура могут варьироваться в зависимости от природы матричной ДНК и концентрации солей в буфере. Для выполнения данной лабораторной работы будет достаточно 3 минут при температуре 96 °C. Температуру отжига определяют путем расчета температуры плавления (Tm) выбранных праймеров. В случае с выбранным праймером начинают отжиг при температуре 50 °C, продолжительность составит 1,5 минуты. Элонгацию проводим при температуре 70 °C в течение 2,5 минут. Количество циклов ПЦР обычно составляет 25—35, но может варьироваться в зависимости от количества вводимой ДНК и желаемого выхода продукта.\n\nЗапишите этап, его продолжительность (в минутах) и температуру для внесения данных в амплификатор:\n(пример ввода: элонгация 2 71)')
    ans3_3 = ['денатурация 3 96', 'отжиг 1,5 50', 'элонгация 2,5 70']
    user_ans3_3 = []  # ответы пользователя

    while True:  # Цикл для повторного ввода в случае ошибки
        user_ans3_3.clear()  # Очистка предыдущих ответов
        for i in range(3):  # ввод и проверка ответов
            ua33 = input().lower()
            user_ans3_3.append(ua33)

        if user_ans3_3 == ans3_3:
            print('Поздравляем! Вы успешно завершили выполнение полимеразной цепной реакции!')
            print('Поздравляем! Вы прошли игру! Спасибо за внимание!')
            break  # Выход из цикла, если ответы верные
        else:
            print('Присутствуют ошибки, перепроверьте и попробуйте еще раз!')
else:
    print('Пройдите второй уровень, чтобы получить необходимые материалы!')
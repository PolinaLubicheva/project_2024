print('Здравствуйте! Вашему вниманию представленя игра "Симулятор лабораторной работы по ПЦР-анализу".')
print('Выберите уровень: ')
print('1. Подготовительный: легкие теоретические вопросы тествового типа (допускается 3 ошибки).')
print('2. Задачи: начальный уровень, решение задач на концентрации (допускается 3 ошибки).')
print('3. ПЦР: схематическое выполнение анализа (повышенный уровень сложности – ошибки недопустимы).')
current_level = int(input('Введи цифру от 1 до 3, чтобы выбрать уровень: '))
levels = [1, 2, 3]
counter_1 = 0
mist = 0
counter_2 = 0
ans_1 = ['а', 'в', 'а', 'г', 'б', 'а', 'б', 'в', 'а', 'г', 'д', 'а', 'а', 'в', 'г', 'г', 'в', 'а', 'б', 'а', 'б', 'а']
per_ans_1 = []

if current_level == 1:
    #переход на первый уровень
    print('Вы выбрали подготовительный уровень!')
    while current_level == 1:
        with open('test_1.txt','r', encoding='utf-8') as f1:
            lines = f1.readlines()
            for line in lines:
                print(line)
                per_ans = input('Введите ответ (одна буква): ')
                if per_ans != ans_1[counter_1]:
                    while mist < 3:
                        print('Присутствует ошибка! Продолжайте решать тест, а пока вот подсказка, вспомните о ней, когда будете перерешивать тест: ')
                        with open('answer_451.txt', 'r', encoding='utf-8') as help_words:
                            helps = help_words.readlines()
                            print(helps[counter_1])
                            mist += 1
                            per_ans = input('Введите ответ (одна буква): ')
                    if mist >= 3:
                        print('Превышено допустимое количество ошибок, пожалуйста, начните заново!')
                        break
                per_ans_1.append(per_ans)
                counter_1 += 1
            if per_ans_1 == ans_1:
                print('Отлично! Тест пройден!')
                cont_ans = input('Хотите проверить себя на более сложном уровне? (Напишите ответ в формате "Да" или "Нет"(без кавычек)): ')
                if cont_ans == 'Да' or cont_ans == 'да':
                    current_level = int(input('Следующий уровень – решение задач, Вы готовы? Если да, введите цифру 2: '))
                    break
                else:
                    print('Хорошая работа! Отдохните!')
                    break
            else:
                print('Стоит попробовать еще раз, где-то есть ошибка!')

if current_level == 2:
    #преход на второй уровень
#На данном уровне с помощью инструкции def мы задаём несколько функций: load_lines_2(), load_answers_2(), main()
    print('Вы выбрали уровень 2 – решение задач!')

#Функция load_lines_2  будет открывать файл с тестом, читать его и  декодировать в формате 'utf-8'. 
#with ставим, чтобы файл сам закрывался, когда работа с ним будет закончена 
#С помощью метода readlines() читаются все строки файла, который указан файл в первом аргументе и сохраняются в список lines_2
#Оператор return возвращает новый список
#В котором каждая строка обработана с использованием метода strip(), удаляющем пробелы (и символы, если указаны) новой строки 
    def load_lines_2(test_2):
        with open(test_2, 'r', encoding='utf-8') as f2:
            lines_2 = f2.readlines()
        return [line_2.strip() for line_2 in lines_2]

#Функция load_answers_2  будет открывать файл с тестом, читать его и  декодировать в формате 'utf-8'. 
#with ставим, чтобы файл сам закрывался, когда работа с ним будет закончена 
#С помощью метода readlines() читаются все строки файла, который указан файл в первом аргументе и сохраняются в список ans_2
#Оператор return возвращает новый список
#В котором каждая строка обработана с использованием метода strip(), удаляющем пробелы (и символы, если указаны) новой строки
    def load_answers_2(correct_answers):
        with open(correct_answers, 'r', encoding='utf-8') as f2:
            ans_2 = f2.readlines()
        return [answer.strip() for answer in ans_2]

#Функция main() является основной частью программы, которая вызывает выше перечисленные функции: 
#lines_2 вызывает функцию load_lines_2() с аргументом 'test_2.txt' - именем файла, из которого нужно загрузить данные
#ans_2 вызывает функцию load_answers_2) с аргументом 'correct_answers.txt' - именем файла, из которого нужно загрузить данные
    def main():  # упрощает чтение программы
        lines_2 = load_lines_2('test_2.txt')
        ans_2 = load_answers_2('correct_answers.txt')
#Задаём переменные: 
    #с лимитом ошибок - t_limit, 
    #счётчиком ошибок - t
    #c индексом текущего вопроса - current_line 
        t_limit = 3
        t = 0
        current_line = 0
#Внутри бесконечного цикла программа будет: 
    #Выводить текущий попрос 
    #И давать поле для ввода ответа
        while True:
            print(lines_2[current_line])
            per_ans_2 = input("Ваш ответ (Введите число): ")
#Когда пользователь вводит и отправляет свой ответ, то метод strip() убирает пробелы
        #Дальше идёт сравнение ответа пользователя и правильного ответа из файла
        #Счётчик ошибок принимает значение 0
        #Индекс текущего вопроса увеличивается на 1
            if per_ans_2.strip().lower() == ans_2[current_line].lower():
                print("Задача решена верно.")
                t = 0
                current_line += 1
                #Идёт сравнение индекса текущего уровня(n) с количеством линий в файле(12)
            #Цикл завершается
                if current_line >= len(lines_2):
                    print(f"""
                            Поздравляем! Вы прошли второй уровень.
                            За успешное прохождение уровня вы получаете необходимые предметы для проведения лабораторной работы:
                            1. Буфер, 
                            2. DNTP, 
                            3. SYBR, 
                            4. Праймер 
                            5. Полимераза,
                            6. Вода""")
                    break
#В случае неверного ответа пользователю сообщают, что он ошибся, 
            #выводят его неправильный ответ и предоставляют подсказку
            #а так же к счётчик ошибок увеличивается на единицу
            else:
                print(f"""Неверный ответ: {per_ans_2}
                    Подсказки:
                    1. Молярность — количество вещества компонента в единице объёма смеси.
                    2. Нормальная концентрация — количество эквивалентов данного вещества в 1 литре смеси.
                    3. Мольная доля — отношение количества молей данного компонента к общему количеству молей всех компонентов.
                    4. Моляльная концентрация — количество растворённого вещества в 1000 г растворителя.""")
                t += 1
                #Если пользователь допускает 3 и более ошибок, то ему выводится сообщение о том, что он должен пройти тест заново
            #Цикл завершается
                if t >= t_limit:
                    print(f"Вы допустили более трёх ошибок в одном задании. Начните тест заново.")
                    break
    #__name__ - хранит имя текущего модуля обычно это самого файла, программы. 
    #__main__ - первый модуль, который запускается
    #Нужно, чтобы при импорте модуля скрипт запускался не сразу, а когда это потребуется пользователю2

    if __name__ == "__main__":
        main()

if current_level == 3:
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
    user_ans3_1 = [] #ответы пользователя

    for i in range(6): #ввод и проверка ответов
        ua31 = input().lower()
        user_ans3_1.append(ua31)
    if user_ans3_1 == ans3_1:
        print('Отлично, продолжим!')
    else:
        print('Присутствуют ошибки, перепроверьте и попробуйте еще раз!')  # повторить ввод ответов пользователем?

    print('Этап 2. Подготовка пробы.\nТеперь поочередно добавляйте нужное количество каждого реагента в пробирку из расчета "нужное количество проб" + "одна запасная проба".')
    ans3_2 = ['буфер 4', 'dntp 4', 'sybr 0,8', 'праймер 4', 'полимераза 0,8', 'вода 22,4']
    user_ans3_2 = [] #ответы пользователя

    for i in range(6): #ввод и проверка ответов
        ua32 = input().lower()
        user_ans3_2.append(ua32)
    if user_ans3_2 == ans3_2:
        print('Отлично, продолжим!')
    else:
        print('Присутствуют ошибки, перепроверьте и попробуйте еще раз!')  # повторить ввод ответов пользователем

    ans322 = input('В пробирку с ДНК добавьте необходимое количество смеси: ')
    if ans322 == 18:
        print('Отлично, продолжим!')
    else:
        print('Присутствуют ошибки, перепроверьте и попробуйте еще раз!')  # повторить ввод ответов пользователем

    print('Этап 3. Амплификация.\nПеред выполнением следующего задания внимательно прочтите текст:\n\nОсновные этапы ПЦР — денатурация, отжиг, элонгация. Начальную стадию денатурации проводят при 94—98 °C в течение 0,5—5 мин. Продолжительность и температура могут варьироваться в зависимости от природы матричной ДНК и концентрации солей в буфере. Для выполнения данной лабораторной работы будет достаточно 3 минут при температуре 96 °C. Температуру отжига определяют путем расчета температуры плавления (Tm) выбранных праймеров. В случае с выбранным праймером начинают отжиг при температуре 50 °C, продолжительность составит 1,5 минуты. Элонгацию проводим при температуре 70 °C в течение 2,5 минут. Количество циклов ПЦР обычно составляет 25—35, но может варьироваться в зависимости от количества вводимой ДНК и желаемого выхода продукта.\n\nЗапишите этап, его продолжительность (в минутах) и температуру для внесения данных в амплификатор:\n(пример ввода: элонгация 2 71)')
    ans3_3 = ['денатурация 3 96', 'отжиг 1,5 50', 'элонгация 2,5 70']
    user_ans3_3 = [] #ответы пользователя

    for i in range(3): #ввод и проверка ответов
        ua33 = input().lower()
        user_ans3_3.append(ans3_3)
    if user_ans3_3 == ans3_3:
        print('Поздравляем! Вы успешно завершили выполнение полимеразной цепной реакции!')
    else:
        print('Присутствуют ошибки, перепроверьте и попробуйте еще раз!')  # возврат в начало

else:
    while current_level not in levels:
        current_level = int(input('Будьте внимательны при вводе номера уровня! Они под номерами 1, 2 и 3!'))

print('Поздравляем! Вы прошли игру! Спасибо за внимание!')
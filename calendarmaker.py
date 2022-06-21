"""Генерация календарей,
Создает календари на месяц, готовые для распечатки, и сохраняет их
в текстовом файле."""

import datetime

# Задаем константы:
DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July',
    'August', 'September', 'October', 'November', 'December')
print('Calendar Maker')

while True: # Цикл для запроса у пользователя года.
    print('Enter the year for the calendar:')
    response = input('> ')

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print('Please enter a numeric year, like 2023.')
    continue

while True: # Цикл для запроса у пользователя месяца.
    print('Enter the month for the calendar, 1-12:')
    response = input('> ')

    if not response.isdecimal():
        print('Please enter a numeric month, like 3 for March.')
        continue

    month = int(response)
    if 1 <= month <= 12:
        break

    print('Please enter a number from 1 to 12.')

def getCalendarFor(year, month):
    calText = '' # calText содержит строковое значение с календарем.

    # Размещаем месяц и год вверху календаря:
    calText += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'

    # Добавляем в календарь метки дней недели:
    # (!) Попробуйте заменить их аббревиатурами: SUN, MON, TUE и т. д.
    calText += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'
    # Горизонтальная линия — разделитель недель:
    weekSeparator = ('+----------' * 7) + '+\n'

    # Пустые строки содержат по десять пробелов между разделителями дней |:
    blankRow = ('|          ' * 7) + '|\n'

    # Получаем первую дату месяца. (Модуль datetime берет на себя
    # все сложные нюансы календарных вычислений.)
    currentDate = datetime.date(year, month, 1)

    # Отнимаем от currentDate по дню, пока не дойдем до воскресенья.
    # (weekday() возвращает для воскресенья 6, а не 0.)
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)

    while True: # Проходим в цикле по всем неделям в месяце.
        calText += weekSeparator

        # dayNumberRow — строка с метками номеров дней:
        dayNumberRow = ''
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1) # Переходим к следующему дню.

        dayNumberRow += '|\n'    # Добавляем вертикальную линию после субботы.
        # Добавляем в текст календаря строку с номерами дней и 3 пустых строки.
        calText += dayNumberRow
        for i in range(3):  # (!) Попробуйте заменить 3 на 5 или 10.
            calText += blankRow

        # Проверяем, закончили ли мы обработку месяца:
        if currentDate.month != month:
            break

    # Добавляем горизонтальную линию в самом низу календаря.
    calText += weekSeparator
    return calText


calText = getCalendarFor(year, month)
print(calText)  # Выводим календарь.

# Сохраняем календарь в текстовом файле:
calendarFilename = 'calendar_{}_{}.txt'.format(year, month)
with open(calendarFilename, 'w') as fileObj:
    fileObj.write(calText)

print('Saved to ' + calendarFilename)

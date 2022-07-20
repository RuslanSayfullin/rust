"""Моделирование индикатора хода выполнения, (c) Sayfullin Ruslan.
 Пример динамического индикатора хода выполнения,
пригодного для использования и в других программах
"""

import random, time

BAR = chr(9608) # Символ 9608 – '█'

def main():
    # Имитируем скачивание:
    print('Progress Bar Simulation, by Al Sweigart')
    bytesDownloaded = 0
    downloadSize = 4096
    while bytesDownloaded < downloadSize:
        # "Скачиваем" случайное количество "байт":
        bytesDownloaded += random.randint(0, 100)

        # Получаем строковое значение с индикатором для этой стадии выполнения:
        barStr = getProgressBar(bytesDownloaded, downloadSize)

        # Не выводим символ новой строки в конце и сразу же сбрасываем
        # строковое значение на экран:
        print(barStr, end='', flush=True)

        time.sleep(0.2) # Небольшая пауза:

        # Выводим символы возврата для перевода курсора в начало строки:
        print('\b' * len(barStr), end='', flush=True)

def getProgressBar(progress, total, barWidth=40):
    """Возвращает строковое значение, соответствующее индикатору хода выполнения
    из barWidth полосок, дошедшему до progress из общего количества total."""

    progressBar = ''    # Индикатор хода выполнения будет строковым значением.
    progressBar += '['  # Добавляем левый конец индикатора хода выполнения.

    # Убеждаемся, что progress находится между 0 и total:
    if progress > total:
        progress = total
    if progress < 0:
        progress = 0

    # Вычисляем количество отображаемых "полосок":
    numberOfBars = int((progress / total) * barWidth)

    progressBar += BAR * numberOfBars   # Добавляем индикатор хода выполнения.
    progressBar += ' ' * (barWidth - numberOfBars)   # Добавляем пустое пространство.
    progressBar += ']'  # Добавляем правый конец индикатора хода выполнения.

    # Вычисляем процент завершения задачи:
    percentComplete = round(progress / total * 100, 1)
    progressBar += ' ' + str(percentComplete) + '%'     # Добавляем значение в процентах.
    # Добавляем числовые значения:
    progressBar += ' ' + str(progress) + '/' + str(total)
    return progressBar  # Возвращаем строковое значение с индикатором хода выполнения.


# Если программа не импортируется, а запускается, выполняем запуск:
if __name__ == '__main__':
    main()

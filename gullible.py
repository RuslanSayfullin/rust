"""Простак, (c) Sayfullin Ruslan.
Как заинтриговать простака на многие часы (программа-шутка).
"""

print('Gullible, by Al Sayfullin Ruslan.')

while True:     # Основной цикл программы.
    print('Do you want to know how to keep a gullible person busy for hours? Y/N')
    response = input('> ')  # Получаем ответ пользователя.
    if response.lower() == 'no' or response.lower() == 'n':
        break   # В случае "no" выходим из цикла.
    if response.lower() == 'yes' or response.lower() == 'y':
        continue    # В случае "yes" продолжаем с начала цикла.
    print('"{}" is not a valid yes/no response.'.format(response))

print('Thank you. Have a nice day!')

import random
from pathlib import Path

def tz_one():

    a = 'До1ро2гие д23рузья, повышение уровня гражданского с4ознания влечет за собой процесс внедре3ния и ' \
        'модернизации направлений пр3огрессивного развития! Таким образ4ом, постоянное информаци5онно-техническое ' \
        'обеспечение нашей деят6ельности иг8рает важную роль в формировании соот85ветствующих условий активизации! ' \
        'Сообр0ажения высшего поря9дка, а так9же сло0жив56шаяся структура организации треб0ует о5т на5с ана567лиза ' \
        'экономической целесообра8зности прини5678маемых реше7ний! '

    array = []

    for char in a:
        if char.isdigit():#метод isdigit() возвращает trye если строка состоит из цифр
            array.append(int(char))

    print(f'сумма чисел: {sum(array)}\n')


def tz_one_part_two():

    a = 'До1ро2гие д23рузья, повышение уровня гражданского с4ознания влечет за собой процесс внедре3ния и ' \
        'модернизации направлений пр3огрессивного развития! Таким образ4ом, постоянное информаци5онно-техническое ' \
        'обеспечение нашей деят6ельности иг8рает важную роль в формировании соот85ветствующих условий активизации! ' \
        'Сообр0ажения высшего поря9дка, а так9же сло0жив56шаяся структура организации треб0ует о5т на5с ана567лиза ' \
        'экономической целесообра8зности прини5678маемых реше7ний! '

    array = []
    n = '' #символьное представление текущего числа
    for char in a:
        if char.isdigit():  # метод isdigit() возвращает trye если строка состоит из цифр
            n += char # если по итерации следующий сивол цифра, присоединяем ее к n
        else:
            if n.isdigit(): #проверка на то есть ли в n цифра
                array.append(int(n))
                n = ''

    print(f'сумма чисел: {sum(array)}\n')


def tz_two():


    i = 7
    array = []
    n = (10)

    for k in range(1, n + 1):  # функция range() позволяет указать какое колличество итераций должен сделать цикл
        array.append(random.randint(1, 50))  # с каждой итерацией append добавляет генерируемое число в конец списка

    if i in array:
        q = array.index(i)
        print(f'число {i} есть в списке, на позиции № {q}')
    else:
        print(f'числа {i} не найдено в списке ')
        
        
  def tz_thre():

    string = r'c:\WebServers\home\testsite\www\myfile.txt'
    print(Path(string).stem) #stem свойство в функции pathlib.Path.stem(), которое возвращает имя файла без его расширения


if __name__ == '__main__':
    tz_one()
    tz_one_part_two()
    tz_two()
    tz_thre()

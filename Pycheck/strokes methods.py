#начинает строку с заглавной буквы
a = 'foo bar'.capitalize()

#все слова с большой буквы
b = 'foo bar'.title()

#переход в верхний регистр и в нижний
с = 'foo bar'.upper()
d = 'foo bar'.lower()

#изменение регистра всех букв
e = 'Foo bar'.swapcase()


#Выравнивание по
#краям (ширина блока, заполняющий символ(пробел по умол.))
'foo bar'.ljust(16, '-') #по левому
'foo bar'.rjust(16, '-') #по правому
'foo bar'.center(16, '-') #по центру


#группа методов, заканчиващихся на strip('simv'), удаляет все
#вхождения указанных символов слева, справа или
#с обоих концов строки(по умолчанию удаляются все пробелы),
#пробелами считаются также всякие \n \r \t и некоторые другие
#литералы
'>><foo bar<>}'.lstrip('<>')
'>><foo bar<>}'.rstrip('}<>')
'>><foo bar<>}'.strip('}<>')


#split('razdelitel', max) разделяет строку на подстроки(в списке)
#по указанному разделителю, если разделитель не указан,
#то строка разделяется пробелами
#может принимать 2 аргумент: максимальное число
#разделителей
'foo,bar'.split(',')
'\t foo bar \t\n  '.split()
'foo.bar.baz.txt'.rsplit('.', 1)  #rsplit для работы
#справа налево


#метод partition('razdelitel') возвращает кортеж из трех элементов:
#подстрока до разделителя, разделитель, подстрока после разделителя
#КОРТЕЖ ВСЕГДА ИЗ ТРЁХ ЭЛЕМЕНТОВ!! (иногда это удобно, т.к.
#split() возвращает не фиксированное количество элементов
'foo,bar,baz'.partition(',')
'foo,bar,baz'.rpartition(',')  #по последнему найденному разделителю


#с помощью метода join(something) можно соединять любую последовательность
#строк(он принимает всё, по чему можно проитерироваться и
#превращает в строку с указанным разделителем.
#join соединяет только строки!!
', '.join(['foo', 'bar', '3'])   #по списку
','.join('foo bar')              #по строке


#метод find('str', start, end) принимает подстроку и возвращает
#индекс её начала в строке. Может принимать
#два дополнительных аргумента: индекс начала поиска
#и индекс конца поиска.
#Если подстрока не нашлась, то возвращает -1
'abracadabra'.find('ra')
'abracadabra'.find('ra', 0, 3)    #возвратит -1


#метод index('str', start, end), тоже самое, что find(), но
#если не находит подстроку, возвращает исключение
'abracadabra'.index('ra')
'abracadabra'.index('ra', 0, 3)   #возвратит исключение


#метод replace('str', 'str, max) заменяет вхождения
#подстроки на заданную строку, по умолчанию - все, 
#но можно ограничить
'abracadabra'.replace('ra', '**')
'abracadabra'.replace('ra', '**', 1)



#методы-предикаты, для проверки строк на условия,
#например, все ли символы в строке числа и др., можно
#найти в документации, если будет нужно































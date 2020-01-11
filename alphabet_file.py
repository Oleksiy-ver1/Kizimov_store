import sys
import os
import random

# 1. Создать строку из маленьких букв, которая содержит весь английский алфавит.
alfavit = 'abcdefghijklmnopqrstuvwxyz'
vowel = 'aeiou'
# alfavit = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# 2. Создать папку ./alphabet/ или проверить, что папка существует.
r_path = r'C:\Users\GTL\PycharmProjects\zozo'
#  и начале строки поставил ключ "r -чистая строка без форматирования" чтоб не читало слеши как объявление спец.символов для работы со строкой, можно еще поставит \\ чтоб эранировать
prodgect1 = 'alfabet'
fullPath = os.path.join(r_path, prodgect1)
# можно было и через сложение строк сделать, но мы же Крутые програмисты, по этому мы будем использовать модуль os, содержащий модуль path  и метод join
if not os.path.exists(fullPath):
    # os.path.exists(fullPath) возвращает True, если path указывает на существующий путь или дескриптор открытого файла, т.е. проверили что папа не существует и создали ее.
    os.mkdir(fullPath)
print(fullPath)
# 3. В папку ./alphabet/ поместить файлы вида a.txt, b.txt, ..., z.txt в которых будет записана строка алфавита, но с заменой буквы из названия файла на заглавную. Пример: для b.txt строка будет aBcde...z

for al in alfavit:
    # всех элементов из строки alfavit
    file_name = fullPath + '\{}.txt'.format(al)
    # собираем имя файла из пути к нему и самого имени(которое соответствует порядковой букве
    with open(file_name, 'w') as f:
        # открываем файл для записи
        alf = alfavit.lower()  # теперь точно все буквы прописые
        alf = alf.replace(al, al.upper())  # заменяем прописную на заглавную
        f.write(str(alf))  # записываем измененную строку в файл

# 4. Переименовать все файлы, в названии которых есть гласная буква на not_a.txt, ... и заменить в строке Abcde...z большие буквы на маленькие и наоборот.
for v in vowel:
    file_name = fullPath + '\{}.txt'.format(v)
    file_name2 = fullPath + '\{}.txt'.format('not_' + v)
    if os.path.exists(file_name2):  # проверяем наличие файла, если есть то удаляем
        os.remove(file_name2)  # удаляем файл
    os.rename(file_name, file_name2)  # переименовываем файл
    f = open(file_name2, 'r')
    al = f.read()
    f.close()

    f = open(file_name2, 'w')
    alUp = al.swapcase()  # переводит символы верхнего регистра в нижний и наоборот
    f.write(alUp)  # записываем измененную строку в файл
    f.close()

# 5. Сделать щелчек Таноса :)  - удалить случайным образом половину всех файлов в этой папке.
# (Половина, не обязательно 1/2. Половина - случайная величина, Болшая половина и Меньшая половина составляют в сумме половину
listDir = os.listdir(fullPath)  # список файлов и директорий в папке.

print("писок файлов ", listDir)

for i in listDir:
    tanos=(-1)**random.randint(1,100) # случайнім образом получаем марку 1 или -1
    if tanos ==1:
        j=fullPath + '\\' + i
        os.remove(j)  # удаляем файл


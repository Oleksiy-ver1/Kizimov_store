# Написать класс FolderInformation с информацией о заданной дериктории.
#
# 1. Инициализация класса.
# В качестве параметра будем использовать относительный путь к папке.
# Пример для папки test, которая находится в той же дирректории, что и запускаемый файл:
# folder_name = os.path.join('test')
# test_folder = FolderInformation(folder_name)
#
# 2. Атрибуты класса:
# Атрибут: files_count
# тип: число,
# описание: количество файлов в папке
# пример:
# print(test_folder.files_count)
# >>> 2
#
# Атрибут: folders_count
# тип: число,
# описание: количество подпапок в папке
# пример:
# print(test_folder.folders_count)
# >>> 1
#
# Атрибут: information
# тип: словарь,
# описание: словарь вида "имя_папки_или_файла": "тип_файл_или_папка"
# {'name_folder': 'folder', 'name_file': 'file', ...}
# Пример:
# print(test_folder.information)
# >>> {'tmp': 'folder', 'test.txt': 'file', 'class_test.py':'file'}
#
# Атрибут: files_value
# тип: словарь,
# описание: словарь вида "имя_файла": "размер_файла_в_байтах" (размер можно получить с помощью модуля os)
# Пример:
# print(test_folder.files_value)
# >>> {'test.txt': 1234, 'class_test.py': 234}
#
# Заполнение атрибутов реализовать при инициализации класса.
#
# 3. Методы класса.
# Метод: clear_folder
# описание: при вызове метода из папки удаляется все ее содержимое
#
# *Метод: safe_clear_folder
# описание: при вызове метода все содержимое папки помещается в архив с именем папки, а затем удаляется все содержимое указанной папки кроме этого архива.


import os
import shutil

class FolderInformation():
    """ class with information about the given directory"""

    def __init__(self, folder_name):
        self.folder_name = folder_name
        files_couter = 0
        folders_counter = 0
        d=dict()
        size=dict()
        for obg in os.listdir(folder_name):
            if os.path.isfile(os.path.join(folder_name, obg)):
                files_couter += 1
                inf="file"
                value = os.path.getsize(os.path.join(folder_name, obg))
                size[obg] = value
            if os.path.isdir(os.path.join(folder_name, obg)):
                folders_counter += 1
                inf="folder"
            d[obg] = inf


        self.files_count = files_couter
        '''returns the number of files in a folder'''
        self.folders_count = folders_counter
        '''returns the number of subfolders in a folder'''
        self.information=d
        '''returns a dictionary of objects and their types'''
        self.files_value=size


    def clear_folder(self):
        for root, dirs, files in os.walk(folder_name):
            for _file in files:
                if os.path.isfile(os.path.join(root, _file)):
                    os.remove(os.path.join(root, _file))
            if folder_name != root and os.path.isdir(root):
                shutil.rmtree(root, ignore_errors=True, onerror=None)


    def safe_clear_folder(self):
        shutil.make_archive(str(arhiv_name), 'gztar', folder_name)
        test_folder.clear_folder()





full_path = os.getcwd()
folder_name = os.path.join(full_path, 'test')
test_folder = FolderInformation(folder_name)
w=os.path.split(folder_name)
arhiv_name = w[-1]
shutil.make_archive(str(arhiv_name), 'gztar', folder_name)

print("files count", test_folder.files_count)
print("directoris count", test_folder.folders_count)
print ("folder information", test_folder.information)
print ("files sizes", test_folder.files_value)
# print ("clear folder", test_folder.clear_folder())
print ("sefe and clear folder", test_folder.safe_clear_folder())

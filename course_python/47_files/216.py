# Чтение из файла
from pathlib import Path
# with open("file.txt") as file_txt:
#     print(file_txt.read())
#     print(file_txt.readlines())


# Запись в файл
# "w" открывает файл для записи, при этом если у файла было содержимое - оно будет перезаписано
with open("new_file.txt", "w") as new_file:
    new_file.write("First line \n")

with open("new_file.txt") as new_file:
    print(new_file.read())

# "a" открывет файл в режиме дозаписи, если были уже созданы записи в файле - они не будет перезаписаны после добавления новой строки
with open("new_file.txt", "a") as new_file:
    new_file.write("Second line\n")

with open("new_file.txt") as new_file:
    print(new_file.read())

if Path("new_file.txt").exists():
    Path("new_file.txt").unlink() # Удаляет файл

print(Path("new_file.txt").exists())


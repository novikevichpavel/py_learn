# ОФрмирование путей на mac и unix

from pathlib import Path

print(Path("user").joinpath("local").joinpath("bin"))
print(Path("usr") / "lcl" / "bin_two")


# Windows

print(Path("C:/").joinpath("Users").joinpath("Pavel"))
print(Path("C:/") / "Users" / "Pavel")



# Проверка наличия определнного файла или дериктории в указанном пути

print(Path("main.py").exists()) # False
print(Path("/Users/pavel/my_folder/python_learning_repository/course_python/32_lambda").exists()) # True



# Проверка на то, является ли искомый файлом или директорией

print(Path("/Users/pavel/my_folder/python_learning_repository/course_python/32_lambda").is_file())
print(Path("/Users/pavel/my_folder/python_learning_repository/course_python/32_lambda").is_dir())

print(Path("/Users/pavel/my_folder/python_learning_repository/course_python/32_lambda/129.py").is_file())
print(Path("/Users/pavel/my_folder/python_learning_repository/course_python/32_lambda/129.py").is_dir())



# Список файлов и папок в директории

for f in Path("/Users/pavel/my_folder/python_learning_repository/course_python").iterdir():
    print(f)



from zipfile import ZipFile
from pathlib import Path

my_path = Path("/Users") / "pavel" / "my_folder" / "python_learning_repository" / "course_python" / "my-files"

Path("./my-files").mkdir()

if not my_path.exists():
    my_path.mkdir()

with open(my_path / "file_one.txt", "w") as my_file:
    my_file.write("This is the first line in this file")

with open(my_path / "file_two.txt", "w") as my_file:
    my_file.write("This is the first line in this file")


# Создание архива
with ZipFile("my-files.zip", mode="w") as zipped_folder:
    print(zipped_folder)
    for file in Path(my_path).iterdir():
        print(file)
        zipped_folder.write(file)


# Распаковка архива
with ZipFile("my-files.zip") as zipped_folder:
    zipped_folder.extractall("my-files-unzipped")
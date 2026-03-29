#  Создание директории. Если директория уже есть - будет вызвана ошибка. Поэтому перед созданием необходимо проверять на наличие

from pathlib import Path

my_dir = Path("/Users") / "pavel" / "my_folder" / "python_learning_repository" / "course_python" / "django"

# Создаст папку
if not my_dir.exists():
    my_dir.mkdir()

# Удалит папку
if my_dir.exists():
    my_dir.rmdir()
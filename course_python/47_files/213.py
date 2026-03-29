# Существует два способа работы с файлами: с помощью библиотеки os; с помощью билиотеки pathlib, которая предлагает объектно-оринетированный опдход работы с файлами

from os import path

print(path.abspath("."))
print(type(path))

from pathlib import Path

print(Path(".").absolute())
print(Path.cwd())
print(type(Path))

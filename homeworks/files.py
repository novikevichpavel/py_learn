from pathlib import Path

new_folder = Path("/Users") / "pavel" / "my_folder" / "python_learning_repository" / "files"

if not new_folder.exists():
    new_folder.mkdir()

with open(new_folder / "first.txt", "w") as first:
    first.write("First line of the first file\n")
    first.write("Second line of the first file\n")
    first.write("Third line of the first file\n")

with open(new_folder / "second.txt", "w") as second:
    second.write("First line of the second file\n")
    second.write("Second line of the second file\n")
    second.write("Third line of the second file\n")
    
with open(new_folder / "first.txt") as first:
    for line in first:
        print(line)

with open(new_folder / "second.txt") as second:
    while True:
        line = second.readline()
        print(line)
        if not line:
            break


if Path(new_folder / "first.txt").exists():
    Path(new_folder / "first.txt").unlink()

if Path(new_folder / "second.txt").exists():
    Path(new_folder / "second.txt").unlink()

if new_folder.exists():
    new_folder.rmdir()

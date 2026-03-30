import csv 

with open("test.csv", "w") as csv_file:
    writer = csv.writer(csv_file, delimiter=";") # Создание врайтера для возможности записи в файл переданный методу. Второй аргумент указывает, какой использовать разделитель, по умолчанию - запятая
    writer.writerow(["user_id", "user_name", "comments_qty"])
    writer.writerow([12, "Pavel", 255])
    writer.writerow([167, "Oksana", 2155])
    writer.writerow([11, "Polina", 17])

with open("test.csv") as csv_file:
    reader = csv.reader(csv_file, delimiter=";") # Второй аргумент не обязателен, но сним снова будут запяты в качестве разделителя
    for line in reader:
        print(line)
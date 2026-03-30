from datetime import datetime, timedelta

my_date = datetime.now()

new_date_time = my_date + timedelta(days=2) # Добавит два дня к текущей дате
print(new_date_time.strftime("%Y-%m-%d %H:%M:%S"))
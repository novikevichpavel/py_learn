import time

# print(time.time())
# print(time.ctime())

# time.sleep(3)

# print("Спустя три секунды из-за задержки, установленной в коде можно увидеть текущее время", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


start_time = time.time()

my_list = list(range(10000000))
print(my_list[1000000])

end_time = time.time()

print(end_time - start_time)
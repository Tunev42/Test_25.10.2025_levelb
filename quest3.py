import random
numbers = []
print("Сколько чисел вы хотите (пример 0 enter 10 enter)?")
n = int(input())
n1 = int(input())
def say_nums():
    print("Сколько чисел вы хотите (пример 0 enter 10 enter)?")
fl = True
try:
    while fl:
        for i in range(random.randint(n, n1)):
            numbers.append(i)
            stop_next = input()
            if stop_next == "stop":
                fl = False
            elif stop_next == "next":
                fl = True
except "stop":
    fl = False
    if numbers / 3:
        print(numbers)






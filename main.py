# quest2
numbers = []
def say_nums():
    print("Введите число")

fl = True

try:
    while fl:
        say_nums()
        nums = int(input())
        numbers.append(nums)
        print("Вы хотите закончить если да напишите 'next' \n"
              " если хотите закончить напишите 'stop'?\n")
        stop = input()
        if stop == "stop":
            print('Вы написали stop')
            fl = False
        elif stop == "next":
            fl = True
except "stop":
    f1 = False
import threading
import random
from math import sqrt


def run():
    print("Привет! Для начала работы необходимо ввести путь к текстовому файлу.\n"
          "Если файл будет указан без пути (например 'text.txt'), "
          "то файл будет автоматически создан в корневой папке программы")
    while True:
        try:
            inpt = str(input("Поле ввода: "))
            if ''.join(reversed(inpt))[:4] != "txt.":
                raise ValueError
        except ValueError:
            print("Введен неверный формат файла.\n"
                  "Файл должен иметь расширение .txt!")
        else:
            break
    return inpt


def is_prime(n):
    prime = True
    i = 2
    while i <= sqrt(n):
        if not n % i:
            prime = False
            break
        i += 1
    if prime:
        return n


def f_l(n):
    fac = 1
    while n > 1:
        fac *= n
        n -= 1
    return fac


class MultithreadingExample:
    def __init__(self, path):
        self.path = path

    def filler(self):
        print("Начало заполнения..")
        plist = [random.randint(0, 10) for _ in range(random.randint(0, 20))]
        with open(self.path, "w+") as f:
            for num in plist:
                f.write(f'{num}\n')
        f.close()
        print(f'Создан список {plist}')

    def find_prime(self):
        print("Начало поиска простых чисел..")
        plist = []
        with open(self.path, "r") as f:
            numbers = f.readlines()
            for num in numbers:
                num.replace("\n", "")
                plist.append(is_prime(int(num)))
        f.close()
        for number in plist:
            if type(number) != int:
                try:
                    while True:
                        plist.remove(number)
                except ValueError:
                    pass
        with open("./Primes.txt", "w+") as f:
            for num in plist:
                f.write(f'{num}\n')
        f.close()
        print(f'Найдены следующие простые числа: {plist}')

    def fucktorials(self):
        print("Начало нахождения факториалов..")
        plist = []
        with open(self.path, "r") as f:
            numbers = f.readlines()
            for num in numbers:
                num.replace("\n", "")
                plist.append(f_l(int(num)))
        f.close()
        with open("./Fac.txt", "w+") as f:
            for num in plist:
                f.write(f'{num}\n')
        f.close()
        print(f'Найденные следующие факториалы: {plist}')


start_case = MultithreadingExample(run())
main_thread = threading.Thread(target=start_case.filler)
prime_thread = threading.Thread(target=start_case.find_prime)
fac_thread = threading.Thread(target=start_case.fucktorials)
main_thread.start()
while main_thread.is_alive():
    pass
prime_thread.start()
fac_thread.start()



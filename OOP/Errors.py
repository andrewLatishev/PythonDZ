class MyExeption(Exception):
    def __str__(self):
        print("My Exception")


try:
    print("Enter the number: ")
    n = int(input())
    assert n >= 0, "Negative n"
    raise TypeError from KeyError
    raise MyExeption
except MyExeption:
    print("MyExeption")
except TypeError:
    print("Ошибка типа")
finally:
    print("Выполнить в любом случае")

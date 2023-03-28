import copy

def counter(func):
    def dec(*args, **kwargs):
        dec.count += 1
        return func(*args, **kwargs)

    dec.count = 0
    return dec

class Snow:
    def __init__(self, countSnowFlake):
        self.countSnowFlake = countSnowFlake

    def __add__(self, other):
        # if not isinstance(other, (int)):
        #     raise ArithmeticError
        # if isinstance(other, Snow):
        #     return Snow(self.countSnowFlake + other.countSnowFlake)
        return Snow(self.countSnowFlake + other)


    def __sub__(self, other):
        # if not isinstance(other, (int)):
        #     raise ArithmeticError
        # if isinstance(other, Snow):
        #     return Snow(self.countSnowFlake - other.countSnowFlake)
        return Snow(self.countSnowFlake - other)


    def __mul__(self, other):
        # if not isinstance(other, (int)):
        #     raise ArithmeticError
        # if isinstance(other, Snow):
        #     return Snow(self.countSnowFlake * other.countSnowFlake)
        return Snow(self.countSnowFlake * other)


    def __truediv__(self, other):
        # if not isinstance(other, (int)):
        #     raise ArithmeticError
        # if isinstance(other, Snow):
        #     return Snow(self.countSnowFlake // other.countSnowFlake)
        return Snow(self.countSnowFlake // other)

    @counter
    def make_snow(self, line):
        original = 'DeepCopyDz'
        cop = copy.deepcopy(original)
        cop = ''
        s = '*'
        for i in range(self.countSnowFlake // line):
            print(f"{s * line}")
        print(f"{s * (self.countSnowFlake % line)}")
        print(cop)

class NewSnow(Snow):
    def __init__(self, countSnowFlake):
        self.countSnowFlake = countSnowFlake


    def __iadd__(self, other):
        # if not isinstance(other, (int)):
        #     raise ArithmeticError
        # if isinstance(other, NewSnow):
        #     return NewSnow(self.countSnowFlake + other.countSnowFlake)
        self.countSnowFlake += other
        return self


    def __isub__(self, other):
        # if not isinstance(other, (int)):
        #     raise ArithmeticError
        # if isinstance(other, NewSnow):
        #     return NewSnow(self.countSnowFlake - other.countSnowFlake)
        self.countSnowFlake -= other
        return self


    def __imul__(self, other):
        # if not isinstance(other, (int)):
        #     raise ArithmeticError
        # if isinstance(other, NewSnow):
        #     return NewSnow(self.countSnowFlake * other.countSnowFlake)
        self.countSnowFlake *= other
        return self


    def __itruediv__(self, other):
        # if not isinstance(other, (int)):
        #     raise ArithmeticError
        # if isinstance(other, NewSnow):
        #     return NewSnow(self.countSnowFlake // other.countSnowFlake)
        self.countSnowFlake //= other
        return self

    @counter
    def make_snow(self, max_height: int):
        num_of_columns = self.countSnowFlake // max_height
        remainder = self.countSnowFlake % max_height
        s = '*'
        for i in range(remainder):
            print(f'{s * (num_of_columns + 1)}')
        for i in range(max_height - remainder):
            print(f'{s * num_of_columns}')

try:
    snow = Snow(30)
    #snow = snow + '5'
    #snow = snow + 'Winter'
    snow.make_snow(10)
    snow.make_snow(20)
    nsnow = NewSnow(33)
    nsnow += 3
    nsnow.make_snow(4)
    print(f'Функция make_snow класса Snow использовалась {snow.make_snow.count} раз')
    print(f'Функция make_snow класса NewSnow использовалась {nsnow.make_snow.count} раз')
except (TypeError):
    print("Неверный тип прибавляемого аргумента")

class Snow:
    def __init__(self, countSnowFlake):
        self.countSnowFlake = countSnowFlake

    def __add__(self, other):
        if not isinstance(other, (int)):
            raise ArithmeticError
        if isinstance(other, Snow):
            return Snow(self.countSnowFlake + other.countSnowFlake)
        return Snow(self.countSnowFlake + other)

    def __sub__(self, other):
        if not isinstance(other, (int)):
            raise ArithmeticError
        if isinstance(other, Snow):
            return Snow(self.countSnowFlake - other.countSnowFlake)
        return Snow(self.countSnowFlake - other)

    def __mul__(self, other):
        if not isinstance(other, (int)):
            raise ArithmeticError
        if isinstance(other, Snow):
            return Snow(self.countSnowFlake * other.countSnowFlake)
        return Snow(self.countSnowFlake * other)

    def __truediv__(self, other):
        if not isinstance(other, (int)):
            raise ArithmeticError
        if isinstance(other, Snow):
            return Snow(self.countSnowFlake // other.countSnowFlake)
        return Snow(self.countSnowFlake // other)

    def make_snow(self, line):
        for i in range(self.countSnowFlake // line):
            print("*" * line)
        print("*" * (self.countSnowFlake % line))


class NewSnow(Snow):
    def __iadd__(self, other):
        if not isinstance(other, (int)):
            raise ArithmeticError
        if isinstance(other, NewSnow):
            return NewSnow(self.countSnowFlake + other.countSnowFlake)
        return NewSnow(self.countSnowFlake + other)

    def __isub__(self, other):
        if not isinstance(other, (int)):
            raise ArithmeticError
        if isinstance(other, NewSnow):
            return NewSnow(self.countSnowFlake - other.countSnowFlake)
        return NewSnow(self.countSnowFlake - other)

    def __imul__(self, other):
        if not isinstance(other, (int)):
            raise ArithmeticError
        if isinstance(other, NewSnow):
            return NewSnow(self.countSnowFlake * other.countSnowFlake)
        return NewSnow(self.countSnowFlake * other)

    def __itruediv__(self, other):
        if not isinstance(other, (int)):
            raise ArithmeticError
        if isinstance(other, NewSnow):
            return NewSnow(self.countSnowFlake // other.countSnowFlake)
        return NewSnow(self.countSnowFlake // other)

    def make_snow(self, max_height: int):
        num_of_columns = self.countSnowFlake // max_height
        remainder = self.countSnowFlake % max_height
        for i in range(remainder):
            print('*' * (num_of_columns + 1))
        for i in range(max_height - remainder):
            print('*' * num_of_columns)


try:
    snow = Snow(29)
    # snow = snow + 5
    # #snow = snow + 'Winter'
    snow.make_snow(10)
    NewSnow = NewSnow(55)
    NewSnow.make_snow(10)
except (TypeError):
    print("Неверный тип прибавляемого аргумента")

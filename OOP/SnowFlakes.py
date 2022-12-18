class Snow:
    def __init__(self, countSnowFlake):
        self.countSnowFlake = countSnowFlake

    def __add__(self, other):
        if not isinstance(other, (Snow, int)):
            raise ArithmeticError
        if isinstance(other, Snow):
            return Snow(self.countSnowFlake + other.countSnowFlake)
        return Snow(self.countSnowFlake + other)

    def __sub__(self, other):
        if not isinstance(other, (Snow, int)):
            raise ArithmeticError
        if isinstance(other, Snow):
            return Snow(self.countSnowFlake - other.countSnowFlake)
        return Snow(self.countSnowFlake - other)

    def __mul__(self, other):
        if not isinstance(other, (Snow, int)):
            raise ArithmeticError
        if isinstance(other, Snow):
            return Snow(self.countSnowFlake * other.countSnowFlake)
        return Snow(self.countSnowFlake * other)

    def __truediv__(self, other):
        if not isinstance(other, (Snow, int)):
            raise ArithmeticError
        if isinstance(other, Snow):
            return Snow(self.countSnowFlake // other.countSnowFlake)
        return Snow(self.countSnowFlake // other)

    def make_snow(self, column):
        for i in range(self.countSnowFlake // column):
            print("*" * column)
        print("*" * (self.countSnowFlake % column))


snow = Snow(19)
snow.make_snow(5)

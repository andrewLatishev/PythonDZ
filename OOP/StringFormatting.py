4 способа

from string import Template
class Student:
    def __init__(self, name, group, mark):
        self.name = name
        self.group = group
        self.mark = mark

    def __str__(self):
        tmp = Template("#$number: Name: $name, group: $group, mark: $mark")
        return "Name: %s, group: %d, mark: %d" % (self.name, self.group, self.mark) + "\n" \
    + "#{number} Name: {0}, group: {1}, mark: {2}".format(self.name, self.group, self.mark, number = 2) + "\n" \
    + f"#{1*3} Name: {self.name}, group: {self.group}, mark: {self.mark}" + "\n" \
    + tmp.substitute(name = self.name, group = self.group, mark = self.mark, number = 4)

Danila = Student("Danila", 112, 5)
print(Danila)

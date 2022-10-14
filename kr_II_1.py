#2
from datetime import datetime

class Date:

    def __init__(self, day, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    def change(self):
        if self.month == 0 or self.year == 0:
            date = datetime.strptime(self.day, "%d.%m.%Y")
            return date.strftime("%d %B %Y")
        else:
            date = datetime.strptime(str(self.day) + " " + self.month + " " + str(self.year), "%d %B %Y")
            return date.strftime("%d.%m.%Y")

    def write(self):
        return self.change()


pt1 = Date("11.12.2022")
print(pt1.write())
pt2 = Date(11, "December", 2003)
print(pt2.write())

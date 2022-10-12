class Text:

    def __init__(self):
        f = open("data.txt")
        self.filetext = f.readlines()
        f.close()

    def lines(self):
        return len(self.filetext)

    def words(self):
        words = 0
        for line in self.filetext:
            words += len(line.split())
        return words

    def symbols(self):
        symbols = 0
        for line in self.filetext:
            for i in line.split():
                symbols += len(i)
        return symbols

    def write(self):
        return self.lines(), self.words(), self.symbols()


fl = Text()
print(fl.write())

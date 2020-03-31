class Nstr(str):
    def __sub__(self,string):
        for i in range(len(string)):
            if string[i] in self:
                self = self.replace(string[i],'')
        return str(self)

a = Nstr('abcdefghijklmnopqrstuvwxyz')
b = Nstr('abcdefghijk')
print(a - b)
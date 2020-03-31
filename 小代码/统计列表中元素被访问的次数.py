class Countlist:
    def __init__(self, *args):
        self.values = [x for x in args ]
        self.count = {}.fromkeys(range(len(self.values)),0)

    def __len__(self):
        return len(self.values)

    def __getitem__(self,key):
        self.count[key] += 1
        return self.values[key]

c1 = Countlist(1,3,5,7,9)
c2 = Countlist(2,4,6,8,10)
c1[1]
c2[1]
c1[1]+c2[2]
print(c1.count)
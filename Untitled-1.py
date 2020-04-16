import pandas as pd

filename = 'HW03.xlsx'
data = pd.read_excel(filename)

class Classify:
    def __init__(self, delimits, x):
        self.delimits = delimits
        self.x = x
    def outer(self):
        def inner():
            for i , delimit in enumerate(self.delimits):
                if x >= delimit:
                    n = i
                else:
                    pass
            pass
            return  n
        return inner
pass

delimits = [0, 5, 10, 15]
List = []
for x in data["Al2O3"]:
    List.append(Classify(delimits,x).outer()())
pass


# c = Classify(delimits,data["Al2O3"]).outer()
# r = map(c, delimits, data["Al2O3"])
# l = list(r)



# r = map(Classify.outer(),delimits, data["Al2O3"])
##----------------------------------------------------------------------------------------------


##----------------------------------------------------------------------------------------------類別的用法










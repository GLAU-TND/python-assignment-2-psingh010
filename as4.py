class MyException(Exception):
    def __init__(self,v):
        self.v=v
    def __str__(self):
        return self.v

a=int(input())
b=int(input())
def Xyz(a,b):
    return a+b
if Xyz(a,b) >150:
    print(Xyz(a,b))
else:
    raise MyException('Custom Exception Occured')

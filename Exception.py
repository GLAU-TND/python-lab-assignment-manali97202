##1
class MyException(Exception):
    def __init__(self,v):
        self.v=v
    def __str__(self):
       return self.v
    def xyz(self,a,b):
        s=a+b
        if s<150:
            raise ValueError('Custom Exception Occured')
        else:
            return s      
a = MyException('Custom Exception Occured')
print(a)
r=a.xyz(14,9)
print(r)


##2
class Manali(Exception):
    try:
        c=3+'ddd'
        print(c)
    except TypeError as e:
        print(e)
    try:
        s=int('sssdddsdsdds')
    except ValueError as e:
        print(e)
    try:
        s='manali'
        s.append(22)
    except AttributeError as e:
        print(e)

##3:
a=input()
try:
    print(a)
except:
    print("Error")

























    

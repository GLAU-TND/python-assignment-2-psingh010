a='34,67,55,33,12,98'
print(list(a.split(',')))
print(tuple(a.split(',')))

b=sorted('without,hello,bag,world'.split(','))
for i in  b:
    print(i,end=',')
s='green-red-yellow-back-white'.split("-")
a=''
s.sort()
for i in s:
    a=a+i+'-'
print(a.strip('-'))

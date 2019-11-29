f2=open('c.txt','w')
f=open('a.txt')
f1=open('b.txt')
a=f.readlines()
b=f1.readlines()
for i in range(len(a)):
    f2.write(a[i][:-1]+'\t'+b[i])
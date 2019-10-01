l = list(map(int,input().split(',')))
k = int(input())


def contiguoussum(l1, k1):
    for i in range(len(l1)):
        s=0
        for j in range(i,len(l1)):
            s = s+l1[j]
            if s == k1:
                return l1[i:j+1]
    return None


print(contiguoussum(l, k))



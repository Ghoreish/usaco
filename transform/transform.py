"""
ID: ali99gh1
LANG: PYTHON3
TASK: transform
"""
f=open("transform.in","r")
g=open("transform.out","w")
def one(x):
    l=[]
    for i in range(len(x)):
        a=[]
        for j in range(len(x)-1,-1,-1):
            a.append(x[j][i])
        l.append(a)
    return l
def two(x):
    l=one(one(x))
    return l
def three(x):
    l=one(two(x))
    return l
def four(x):
    l = []
    for i in range(len(x)):
        a = []
        for j in range(len(x) - 1, -1, -1):
            a.append(x[i][j])
        l.append(a)
    return l
def five(x):
    l=[]
    l.append(one(four(x)))
    l.append(two(four(x)))
    l.append(three(four(x)))
    return l
def check(x,y):
    if one(x)==y:
        return 1
    elif two(x)==y:
        return 2
    elif three(x)==y:
        return 3
    elif four(x)==y:
        return 4
    elif y in five(x):
        return 5
    elif x==y:
        return 6
    else:
        return 7

n=int(f.readline()[:-1])
l1=[]
for i in range(0,n):
    l1.append(list(f.readline()[:-1]))
l2=[]
for i in range(0,n):
    l2.append(list(f.readline()[:-1]))
a=check(l1,l2)
g.write(str(a))
g.write("\n")
g.close()
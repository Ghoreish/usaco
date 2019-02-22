"""
ID: ali99gh1
LANG: PYTHON3
TASK: beads
"""
f=open("beads.in","r")
g=open("beads.out","w")
def left1(x):
    l="begin"
    n=0
    for i in x:
        if i==l or l=="begin" or i=="w":
            n+=1
        else:
            break
        if i == "w":
            continue
        l=i
    return n
def left2(x):
    l="begin"
    n=0
    t=0
    for i in x:
        if i==l or l=="begin" or i=="w":
            n+=1
        else:
            if t==0:
                t=1
                n+=1
                l=i
            else:
                break
        if i == "w":
            continue
        l=i
    return n
def right1(x):
    l = "begin"
    n = 0
    for i in range(-1,-len(x),-1):
        if x[i] == l or l == "begin" or x[i] == "w":
            n += 1
        else:
            break
        if x[i] == "w":
            continue
        l = x[i]
    return n
def right2(x):
    l="begin"
    n=0
    t=0
    for i in range(-1, -len(x), -1):
        if x[i]==l or l=="begin" or x[i]=="w":
            n+=1
        else:
            if t==0:
                t=1
                n+=1
                l=x[i]
            else:
                break
        if x[i] == "w":
            continue
        l=x[i]
    return n
def findmuch(x):
    l=[0]
    if x[-1]==i[0] and x[-1]!="w":
        h=[]
        if right1(x) == len(x)-1 or left1(x) == len(x)-1 or left2(x) == len(x)-1 or right2(x) == len(x)-1:
            h.append(len(x))
        else:
            h.append(left1(x)+right2(x))
            h.append(left2(x)+right1(x))
        l.append(max(h))
    else:
        if right1(x) == len(x)-1 or left1(x) == len(x)-1 or left2(x) == len(x)-1 or right2(x) == len(x)-1:
            l.append(len(x))
        else:
            l.append(left1(x)+right1(x))
    return max(l)
def slicer(x):
    l=[]
    for i in range(len(x)):
        l.append(x[i:]+x[:i])
    return l
f.readline()
x=f.readline()
if "\n" in x:
    x=x[:-1]
n=0
for i in x:
    if i=="w":
        n+=1
b=slicer(x)
gg=[]
for i in b:
    gg.append(findmuch(i))
g.write(str(max(gg))+"\n")
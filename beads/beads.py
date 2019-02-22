"""
ID: ali99gh1
LANG: PYTHON3
TASK: beads
"""
f=open("beads.in","r")
g=open("beads.out","w")
def check(l):
    ml=[]
    for i in l:
        if i=="w":
            ml.append(0)
    nl=[]
    while True:
        nl.append([])
        for i in ml:
            nl[-1].append(i)
        ml[-1]+=1
        while 2 in ml:
            if all(ml)==1:
                break
            for i in range(len(ml)):
                if ml[i]==2:
                    ml[i]=0
                    ml[i-1]+=1
        if all(ml) == 1:
            nl.append([])
            for i in ml:
                nl[-1].append(i)
            break
    return nl
def makebeads(x):
    if "w" in x:
        yy=[]
        h=check(x)
        for i in h:
            n=0
            y=""
            for j in x:
                if j=="w":
                    if i[n]==0:
                        y+="b"
                    else:
                        y+="r"
                    n+=1
                else:
                    y+=j
            yy.append(y)
    else:
        yy=[x]
    return yy
def left1(x):
    l="begin"
    n=0
    for i in x:
        if i==l or l=="begin":
            n+=1
        else:
            break
        l=i
    return n
def left2(x):
    l="begin"
    n=0
    t=0
    for i in x:
        if i==l or l=="begin":
            n+=1
        else:
            if t==0:
                t=1
                n+=1
                l=i
            else:
                break
        l=i
    return n
def right1(x):
    l = "begin"
    n = 0
    for i in range(-1,-len(x),-1):
        if x[i] == l or l == "begin":
            n += 1
        else:
            break
        l = x[i]
    return n
def right2(x):
    l="begin"
    n=0
    t=0
    for i in range(-1, -len(x), -1):
        if x[i]==l or l=="begin":
            n+=1
        else:
            if t==0:
                t=1
                n+=1
                l=x[i]
            else:
                break
        l=x[i]
    return n
def findmuch(x):
    l=[0]
    a=makebeads(x)
    for i in a:
        if i[-1]==i[0]:
            h=[]
            if right1(i)==len(i) or left1(i)==len(i) or left2(i)==len(i) or right2(i)==len(i):
                h.append(len(i))
            else:
                h.append(left1(i)+right2(i))
                h.append(left2(i)+right1(i))
            l.append(max(h))
        else:
            if right1(i) == len(i) or left1(i) == len(i) or left2(i) == len(i) or right2(i) == len(i):
                l.append(len(i))
            else:
                l.append(left1(i)+right1(i))
    return max(l)
def makewstan(x):
    y=""
    t=0
    kk=0
    if x == "w" * len(x):
        for i in range(len(x)):
            y+="r"
        return y
    for i in range(0,len(x)):
        if x[i]=="w":
            try:
                mmm=x[i+1]
            except:
                mmm=x[0]
            if t==0 and x[i-1]+mmm in ["rb","br"]:
                t=1
                y+="w"
            else:
                if x[i-1]=="w":
                    y+=mmm
                elif mmm=="w":
                    y+=x[i-1]
                else:
                    if x[i-1]+mmm in ["rr","bb"]:
                        y+=x[i-1]
                    else:
                        y+="w"
        else:
            y+=x[i]
    return y
def slicer(x):
    l=[]
    for i in range(len(x)):
        l.append(x[i:]+x[:i])
    return l
def makes2(x):
    y=""
    for i in x:
        if i=="w":
            y+="r"
        else:
            y+=i
    return y
f.readline()
x=f.readline()
if "\n" in x:
    x=x[:-1]
a=makewstan(x)
n=0
for i in a:
    if i=="w":
        n+=1
print(a)
if n>=23:
    a=a[:8]+makes2(a[8:-8])+a[-8:]
print(a)
b=slicer(a)
gg=[]
for i in b:
    gg.append(findmuch(i))
g.write(str(max(gg))+"\n")
"""
ID: ali99gh1
LANG: PYTHON3
TASK: numtri
"""

f=open("numtri.in","r")
o=open("numtri.out","w")
n=int(f.readline()[:-1])
l=[]
for i in range(n):
    g=f.readline()[:-1].split()
    k=[]
    for j in g:
        k.append(int(j))
    l.append(eval(str(k)))
oo=[]
def sumpos(x,y):
    global n
    t=0
    a=l[x][y]
    for i in range(x+1,n):
        t+=1
        for j in range(y,y+t+1):
            a+=l[i][j]
    return a
def whichpos(x,y):
    if sumpos(x+1,y) > sumpos(x+1,y+1):
        return (x+1,y)
    elif sumpos(x+1,y) == sumpos(x+1,y+1):
        if sumpos(x + 1, y)-l[x+1][y] > sumpos(x + 1, y + 1)-l[x+1][y+1]:
            return (x + 1, y)
        else:
            return (x + 1, y + 1)
    else:
        return (x+1,y+1)
def y(a,n):
    if n==0:
        d=1
        z=0
        t=l[0][0]
        for i in a:
            if i =="R":
                z+=1
            t+=l[d][z]
            d+=1
        oo.append(t)
    else:
        n-=1
        for i in "LR":
            a+=i
            y(a,n)
            a=a[:-1]
if n<25:
    y("",n-1)
else:
    pos = (0, 0)
    s = l[0][0]
    while pos[0] < n - 1 and pos[1] < n - 1:
        pos = whichpos(pos[0], pos[1])
        s += l[pos[0]][pos[1]]
    oo.append(s)
o.write(str(max(oo))+"\n")
f.close()
o.close()
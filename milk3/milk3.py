"""
ID: ali99gh
LANG: PYTHON3
TASK: milk3
"""
def ber(x,y,m):
    t=[m[0],m[1],m[2]]
    global v
    if t[x]>v[y]-t[y]:
        t[x]-=(v[y]-t[y])
        t[y]=v[y]
    else:
        t[y]+=t[x]
        t[x]=0
    return t
f=open("milk3.in","r")
g=open("milk3.out","w")
a,b,c=f.read()[:-1].split()
a,b,c=int(a),int(b),int(c)
v=[a,b,c]
h=[]
for i in range(3):
    for j in range(3):
        if i!=j:
            h.append((i,j))
l=[0,0,c]
s=set()
r=set()
s.add(str(l))
r.add(str(l))
while True:
    for i in r:
        for j in h:
            m=ber(j[0],j[1],eval(i))
            if str(m) not in s:
                s.add(str(m))
    if s==r:
        break
    r=set()
    for i in s:
        r.add(i)
o=[]
for i in s:
    z=eval(i)
    if z[0]==0:
        o.append(z[2])
o.sort()
e=""
for i in o:
    e+=(str(i)+" ")
g.write(e[:-1]+"\n")
g.close()
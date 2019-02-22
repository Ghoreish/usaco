""""
ID: ali99gh1
LANG: PYTHON3
TASK: wormhole
"""
def goright(x):
    global n
    for i in l:
        if i[0]>x[0] and i[1]==x[1]:
            return (i[0],i[1])
    return False
def check(d):
    for i in l:
        t=1
        a=i
        while t==1:
            a=d[a]
            x=goright(a)
            if x==False:
                t=0
            else:
                a=x
            if a==i and x!=False:
                return True
    return False
def make():
    total=0
    for i in dic:
        if dic[i]==0:
            dic[i]=1
            break
    t=0
    for s in dic:
        if dic[s]==0:
            t+=1
    if t==0:
        if check(dic):
            return 1
        else:
            return 0
    for j in dic:
        if dic[j]==0:
            dic[i]=j
            dic[j]=i
            total+=make()
            dic[i]=dic[j]=0
    return total
f=open("wormhole.in","r")
g=open("wormhole.out","w")
n=int(f.readline()[:-1])
l=[]
for i in range(n):
    a=f.readline()[:-1].split()
    l.append((int(a[0]),int(a[1])))
l.sort()
dic={}
for i in l:
    dic[i]=0
bbb=make()
g.write(str(bbb)+"\n")
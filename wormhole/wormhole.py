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
f=open("wormhole.in","r")
g=open("wormhole.out","w")
n=int(f.readline()[:-1])
l=[]
for i in range(n):
    a=f.readline()[:-1].split()
    l.append((int(a[0]),int(a[1])))
l.sort()
nn=[]
for i in range(n):
    nn.append(i)
t=0
mm=[]
for i in nn:
    mm.append(i)
ll=[]
while t==0:
    for i in range(n-1):
        nn[i],nn[i+1]=nn[i+1],nn[i]
        ll.append([])
        for k in nn:
            ll[-1].append(k)
        if mm==nn:
            t=1

lll=[]
bbb=0
ccc=0
for i in ll:
    dic={}
    for k in nn:
        dic[l[k]] = []
    for j in range(int((len(i)))):
        dic[l[i[j]]]=l[i[len(i)-(j)-1]]
    if check(dic)==True and dic not in lll:
        lll.append(eval(str(dic)))
        bbb+=1
    dic = {}
    for k in nn:
        dic[l[k]] = []
    for j in range(0,int((len(i)-1)),2):
        dic[l[i[j]]] = l[i[j+1]]
        dic[l[i[j+1]]] = l[i[j]]
    if check(dic) == True and dic not in lll:
        lll.append(eval(str(dic)))
        bbb += 1
g.write(str(bbb)+"\n")
"""
ID: ali99gh1
LANG: PYTHON3
TASK: milk
"""
f=open("milk.in","r")
g=open("milk.out","w")
a=f.readline()[:-1]
b=a.split()
need=int(b[0])
n=int(b[1])
l=[]
for i in range(n):
    a = f.readline()[:-1]
    b = a.split()
    l.append([int(b[0]),int(b[1])])
l.sort()
n=0
pay=0
while need>0:
    a=l[n]
    if a[1]<=need:
        need-=a[1]
        pay+=a[0]*a[1]
    else:
        pay+=need*a[0]
        need=0
    n+=1
g.write(str(pay)+"\n")
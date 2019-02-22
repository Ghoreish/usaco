"""
ID: ali99gh1
LANG: PYTHON3
TASK: ariprog
"""
import time
#print(time.strftime("%H:%M:%S"))
def isit(a,d):
    global n,k,o
    t=0
    for i in range(n):
        if a not in k:
            return False
        a+=d
    return True
f=open("ariprog.in","r")
g=open("ariprog.out","w")
n=int(f.readline()[:-1])
m=int(f.readline()[:-1])
k=set()
for i in range(m+1):
    for j in range(i,m+1):
        h=i**2+j**2
        if h not in k:
            k.add(h)
ss=set()
for i in k:
    if i <= m*m//2:
        ss.add(i)
if m<100:
    ss=k
#print(max(ss))
#print(len(k),2*m**2//(n-1)+2)
t=0
o=[]
#print(max(k))
#print(len(k),len(ss))
for d in range(1,m*10+m+m):
    for a in ss:
        if isit(a,d):
            o.append([d,a])
            t=1
o.sort()
if len(o)==0:
    g.write("NONE\n")
else:
    for i in o:
        g.write(str(i[1])+" "+str(i[0])+"\n")
f.close()
g.close()
#print(time.strftime("%H:%M:%S"))
"""
ID: ali99gh1
LANG: PYTHON3
TASK: barn1
"""
f=open("barn1.in","r")
g=open("barn1.out","w")
a=f.readline()[:-1].split()
t=int(a[0])
s=int(a[1])
n=int(a[2])
l=[]
for i in range(n):
    l.append(int(f.readline()[:-1]))
l.sort()
ll=[]
for i in range(len(l)-1):
    ll.append(l[i+1]-l[i]-1)
ll.sort()
while len(ll)>=t:
    ll.remove(ll[0])
al=l[-1]-l[0]+1
for i in ll:
    al-=i
g.write(str(al)+"\n")
g.close()
f.close()

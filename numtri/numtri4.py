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
k=set()
def make(x,y,a):
    if x<n-1 and y<n-1:
        for i in [(x+1,y),(x+1,y+1)]:
            a+=l[i[0]][i[1]]
            make(i[0],i[1],a)
            a-=l[i[0]][i[1]]
    else:
        k.add(a)
make(0,0,l[0][0])
o.write(str(max(k))+"\n")
f.close()
o.close()
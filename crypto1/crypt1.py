"""
ID: ali99gh1
LANG: PYTHON3
TASK: crypt1
"""
def check(notin,x):
    x=list(str(x))
    for i in notin:
        if i in x:
            return False
    return True
notin=list("0123456789")
f=open("crypt1.in","r")
g=open("crypt1.out","w")
f.readline()
k=f.readline()[:-1]
k=k.split()
for i in k:
    notin.remove(i)
n=0
for i in range(111,999):
    for j in range(11,99):
        a=(j%10)*i
        b=int(j/10)*i
        e=i*j
        if check (notin,i) and check(notin,j) and check(notin,a) and check(notin,b) and len(str(a))==3 and len(str(b))==3 and len(str(e))==4 and check(notin,e):
            n+=1
g.write(str(n)+"\n")
f.close()
g.close()
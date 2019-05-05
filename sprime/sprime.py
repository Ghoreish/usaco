"""
ID: ali99gh1
LANG: PYTHON3
TASK: sprime
"""
def cp(x):
    x=int(x)
    if x<2:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
f=open("sprime.in","r")
g=open("sprime.out","w")
n=int(f.read()[:-1])
f.close()
l1=[2,3,5,7]
l2=[]
while True:
    if n==1:
        l2=eval(str(l1))
        break
    for i in l1:
        for j in range(10):
            a=int(str(i)+str(j))
            if cp(a)==True:
                l2.append(a)
    t=0
    for i in l2:
        if len(str(i))!=n:
            t=1
    if t==0:
        break
    else:
        l1=eval(str(l2))
        l2=[]
l2.sort()
for i in l2:
    g.write(str(i))
    g.write("\n")
g.close()
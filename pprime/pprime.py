"""
ID: ali99gh1
LANG: PYTHON3
TASK: pprime
"""
f=open("pprime.in","r")
g=open("pprime.out","w")
a,b=f.readline()[:-1].split()
a,b=int(a),int(b)
l=set()
def pris(x):
    if x==2:
        return True
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True
l.add(2)
for i in range(1,10,2):
    l.add(i)
    l.add(int(str(i)+str(i)))
    for j in range(10):
        l.add(int(str(i)+str(j)+str(i)))
        l.add(int(str(i)))
for i in range(1,10,2):
    for j in range(10):
        l.add(int(str(i)+str(j)+str(j)+str(i)))
        for k in range(10):
            l.add(int(str(i) + str(j) +str(k)+ str(j) + str(i)))
for i in range(1,10,2):
    for j in range(10):
        for k in range(10):
            l.add(int(str(i)+str(j)+str(k)+str(k)+str(j)+str(i)))
            for m in range(10):
                l.add(int(str(i)+str(j)+str(k)+str(m)+str(k)+str(j)+str(i)))

s=[]
primes=set()
for i in l:
    if pris(i)==True:
        primes.add(i)
for i in primes:
    if a<=i and i<=b:
        s.append(i)
s.sort()

for i in s:
    g.write(str(i))
    g.write("\n")
f.close()
g.close()
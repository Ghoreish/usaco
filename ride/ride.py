"""
ID: ali99gh1
LANG: PYTHON3
TASK: ride
"""

def numcal(x):
    l=list("QWERTYUIOPASDFGHJKLZXCVBNM")
    l.sort()
    n=1
    dic={}
    for i in l:
        dic.update({i:n})
        n+=1
    num = 1
    for i in x:
        if i in dic:
            num*=dic[i]
    return num
f=open("ride.in","r")
g=open("ride.out","w")
a=f.readline()
a=numcal(a)
b=f.readline()
b=numcal(b)
if (a-b)%47==0 or (b-a)%47==0:
    g.write("GO\n")
else:
    g.write("STAY\n")
f.close()
g.close()
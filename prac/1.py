a=""
for i in range(9):
    a=a+str(i)
    for j in range(9):
        a=a+str(j)
        for k in range(9):
            a=a+str(k)
            a=a[:-1]
        a=a[:-1]
    a=a[:-1]

def forr(l,a,n):
    nn=n
    for i in l:
        a=a+str(i)
        if nn>1:
            nn-=1
            forr(l,a,nn)
        else:
            print(a)
        a=a[:-1]
        nn=n
l={"A":0,"B":0,"C":0}
def jay(a=""):
    global l
    print(l)
    for i in l:
        if l[i]==0:
            l[i]=1
            a+=i
            jay(a)
            l[i]=0
            a=a[:-1]
    t=0
    for i in l:
        if l[i]==0:
            t+=1
    if t==0:
        print(a)
jay()
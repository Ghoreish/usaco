'''
ID: ali99gh1
LANG: PYTHON3
TASK: milk2
'''
import time
f=open("milk2.in","r")
g=open("milk2.out","w")
n=int(f.readline()[:-1])
dic={}
l1=[]
if n>1:
    for i in range(0,n):
        a=f.readline()[:-1]
        a=a.split(" ")
        a=[int(a[0]),int(a[1])]
        l1.append([a[0],a[1]])
    l1.sort()
    a=int(l1[0][0])
    n1=0
    n2=0
    for i in l1:
        for j in i:
            l1[n1][n2]-=a
            n2+=1
        n2=0
        n1+=1
    l2=[[0,0]]
    for i in l1:
        a=i[0]
        b=i[1]
        nn=0
        op=0
        for j in l2:
            c=j[0]
            d=j[1]
            if (a>=c and b<d) or (a>c and b<=d):
                op=1
        if op==0:
            if a<=l2[-1][1]:
                l2.append([l2[-1][0],b])
                l2.remove(l2[-2])
            else:
                l2.append([a,b])
        while [0,0] in l2:
            l2.remove([0,0])
    l3=[]
    for i in l2:
        l3.append(i[1]-i[0])
    l4=[]
    for i in range(0,len(l2)-1):
        o=(l2[i+1][0]-l2[i][1])
        if o>0:
            l4.append(o)
        else:
            l4.append(0)
else:
    a = f.readline()
    a = a.split(" ")
    a = [int(a[0]), int(a[1])]
    l3=[a[1]-a[0]]
    l4=[0]
if l3==[]:
    maxmilking=0
else:
    maxmilking = max(l3)
if l4==[]:
    maxnotmilking=0
else:
    maxnotmilking=max(l4)
m=str(maxmilking)+" "+str(maxnotmilking)
g.write(m)
g.write("\n")
g.close()
f.close()
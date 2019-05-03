"""
ID: ali99gh1
LANG: PYTHON3
TASK: numtri
"""
import random
f=open("numtri.in","r")
o=open("numtri.out","w")
n=int(f.readline()[:-1])
l=[]
for i in range(n):
    a=f.readline()[:-1].split()
    j=[]
    for k in a:
        j.append(int(k))
    l.append(eval(str(j)))
for i in range(n-2,-1,-1):
    for j in range(len(l[i])):
        l[i][j]+=max([l[i+1][j],l[i+1][j+1]])
o.write(str(l[0][0])+"\n")
f.close()
o.close()
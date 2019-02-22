"""
ID: ali99gh1
LANG: PYTHON3
TASK: combo
"""

f=open("combo.in","r")
g=open("combo.out","w")
n=int(f.readline()[:-1])+1
pass1=f.readline()[:-1].split()
a=(int(pass1[0]),int(pass1[1]),int(pass1[2]))
pass2=f.readline()[:-1].split()
b=(int(pass2[0]),int(pass2[1]),int(pass2[2]))
nn=[]
for i in range(1,n):
    nn.append(i)
n=nn+nn+nn
m=0
l=[]
for i in range(a[0]-3,a[0]+2):
    for j in range(a[1] - 3, a[1] + 2):
        for k in range(a[2] - 3, a[2] + 2):
            if (n[i],n[j],n[k]) not in l:
                l.append((n[i],n[j],n[k]))
                m+=1
for i in range(b[0]-3,b[0]+2):
    for j in range(b[1] - 3, b[1] + 2):
        for k in range(b[2] - 3, b[2] + 2):
            if (n[i],n[j],n[k]) not in l:
                l.append((n[i],n[j],n[k]))
                m+=1
g.write(str(m)+"\n")
f.close()
g.close()
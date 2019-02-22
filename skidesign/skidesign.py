"""
ID: ali99gh1
LANG: PYTHON3
TASK: skidesign
"""
def mini(dic):
    a=101
    for i in dic:
        if dic[i]<=a:
            a=dic[i]
            b=i
    return b
def maxi(dic):
    a = 0
    for i in dic:
        if dic[i] >= a:
            a = dic[i]
            b = i
    return b
f=open("skidesign.in","r")
g=open("skidesign.out","w")
n=int(f.readline()[:-1])
l=[]
for i in range(n):
    l.append(int(f.readline()[:-1]))
l.sort()
mmm=[]
for i in range(0,84):
    a=i
    b=i+17
    nn=0
    for j in l:
        if j>b:
            nn+=(j-b)**2
        elif j<a:
            nn+=(a-j)**2
    mmm.append(nn)
g.write(str(min(mmm))+"\n")
f.close()
g.close()
"""
ID: ali99gh1
LANG: PYTHON3
TASK: gift1
"""
f=open("gift1.in","r")
g=open("gift1.out","w")
n=int(f.readline()[:-1])
l=[]
for i in range(n):
    l.append(f.readline()[:-1])
dic={}
for i in l:
    dic[i]=0
data=f.readline()[:-1]
while data:
    person=data
    data=f.readline()
    paylist=[]
    d=data.split()
    pay=int(d[0])
    num=int(d[1])
    for i in range(num):
        paylist.append(f.readline()[:-1])
    if num!=0:
        dic[person]-=(int(pay/num)*num)
    for i in paylist:
        dic[i]+=int(pay/num)
    data=f.readline()[:-1]
for i in dic:
    g.write(str(i))
    g.write(" ")
    g.write(str(dic[i]))
    g.write("\n")
f.close()
g.close()
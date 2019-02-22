"""
ID: ali99gh1
LANG: PYTHON3
TASK: friday
"""
f=open("friday.in","r")
g=open("friday.out","w")
class Year:
    def __init__(self,n):
        if n%100==0:
            if n%400==0:
                self.kab=True
            else:
                self.kab=False
        else:
            if n%4==0:
                self.kab=True
            else:
                self.kab=False
        if self.kab==True:
            self.l = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            self.l = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def what(n):
    daydic={}
    for i in range(7):
        daydic.update({i:0})
    yearlist=[]
    for i in range(1900,1900+n):
        yearlist.append(Year(i))
    n=1
    for i in yearlist:
        for j in i.l:
            for k in range(1,j+1):
                n=(n+1)%7
                if k==13:
                    daydic[n]+=1
    res=""
    for i in daydic:
        res+=str(daydic[i])
        res+=" "
    return res
inp=f.read()
res=""
for i in inp:
    try:
        res+=i
    except:
        pass
out=what(int(res))
g.write(out[:-1]+"\n")
f.close()
g.close()
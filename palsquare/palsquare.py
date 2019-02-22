"""
ID: ali99gh1
LANG: PYTHON3
TASK: palsquare
"""
def tenton(x,n):
    dic = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J'}
    text=""
    while True:
        text=dic[x%n]+text
        x=int(x/n)
        if x<n:
            if x>0:
                text=dic[x]+text
            break
    return text
def ismir(x):
    l=list(x)
    m=[]
    for i in l:
        m.append(i)
    l.reverse()
    if m==l:
        return True
    else:
        return False
f=open("palsquare.in","r")
g=open("palsquare.out","w")
n=int(f.read()[:-1])
l=[]
for i in range(1,301):
    a=i*i
    b=tenton(a,n)
    if ismir(b):
        g.write(tenton(i,n)+" "+tenton(a,n)+"\n")
f.close()
g.close()
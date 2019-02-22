"""
ID: ali99gh1
LANG: PYTHON3
TASK: namenum
"""
def converttonum(x):
    dic = {'A': 2, 'B': 2, 'C': 2, 'D': 3, 'E': 3, 'F': 3, 'G': 4, 'H': 4, 'I': 4, 'J': 5, 'K': 5, 'L': 5, 'M': 6, 'N': 6, 'O': 6, 'P': 7, 'R': 7, 'S': 7, 'T': 8, 'U': 8, 'V': 8, 'W': 9, 'X': 9, 'Y': 9}
    text=''
    for i in x:
        try:
            text+=str(dic[i])
        except:
            return None
    return int(text)
f=open("namenum.in","r")
g=open("namenum.out","w")
h=open("dict.txt","r")
n=int(f.read()[:-1])
l={}
m=h.readline()
while m:
    m=m[:-1]
    m1=converttonum(m)
    if m1:
        if m1 in l:
            l[m1].append(m)
        else:
            l[m1]=[m]
    m=h.readline()
if n in l:
    for i in l[n]:
        g.write(i)
        g.write("\n")
else:
    g.write("NONE")
    g.write("\n")
g.close()
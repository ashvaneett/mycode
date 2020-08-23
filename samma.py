from itertools import*
from collections import*
for _ in range(int(input())):
    s=input()
    l=[]
    res=["".join(sorted(s[x:y])) for x,y in combinations(range(len(s)+1),r=2)]
    print(res)
    sam=0
    c=set(res)
    for i in c:
        if(res.count(i)>1):
            sam+=res.count(i)//2
    print(sam)

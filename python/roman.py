from string import ascii_uppercase as a
from itertools import product as d
import re
n=range
k=input("Enter Key for ajit: ")
p=input("Enter STring to crypt:")
t=lambda x: x.upper().replace('J','I')
s=[]
for _ in t(k+a):
 if _ not in s and _ in a:
  s.append(_)
m=[s[i:i+5] for i in n(0,len(s),5)]
e={r[i]+r[j]:r[(i+1)%5]+r[(j+1)%5] for r in m for i,j in d(n(5),repeat=2) if i!=j}
e.update({c[i]+c[j]:c[(i+1)%5]+c[(j+1)%5] for c in zip(*m) for i,j in d(n(5),repeat=2) if i!=j})
e.update({m[i1][j1]+m[i2][j2]:m[i1][j2]+m[i2][j1] for i1,j1,i2,j2 in d(n(5),repeat=4) if i1!=i2 and j1!=j2})
l=re.findall(r'(.)(?:(?!\1)(.))?',''.join([_ for _ in t(p) if _ in a]))
print(''.join(e[a+(b if b else 'X')] for a,b in l))
from collections import defaultdict
global H,I,M,Opt

def recubest(c):
    global H,I,M
    if not c in Opt:
        m=0
        if not c[1]==H-1:
            for b in range(H):
                if b==c[0]:
                    m=max(m,recubest((c[0],c[1]+1)))
                elif c[1]+I<H:
                    m=max(m,recubest((b,c[1]+I)))
        Opt[c]=m+M[c]
    return Opt[c]
    

M=defaultdict(int)
Opt=defaultdict(int)
[N,H,I]=map(int,input().split())
for i in range(N):
    u=list(map(int,input().split()))[1:]
    for ui in u:
        M[(i,ui-1)]+=1
        
m=0
for i in range(H):
    m=max(m, recubest((i,0)))
        
print(m)
     

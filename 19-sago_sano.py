print("SAGO + SANO = FELIC")
f = 1
pocet = 0
for s in range(5,10):
    for a in range (0,10):
        if (a!=s) and (a!=f):
            for g in range(0,10):
                if (g!=s) and (g!=a) and (g!=f):
                    for o in range(0,10):
                        if (o!=s) and (o!=a) and (o!=f) and (o!=g):
                            for n in range(0,10):
                                if (n!=s) and (n!=a) and (n!=f) and (n!=g) and (n!=o):
                                    for e in range(0,10):
                                        if (e!=s) and (e!=a) and (e!=f) and (e!=g) and (e!=o) and (e!=n):
                                            for l in range(0,10):
                                                if (l!=s) and (l!=a) and (l!=f) and (l!=g) and (l!=o) and (l!=n) and (l!=e):
                                                     for i in range (0,10):
                                                        if (i!=s) and (i!=a) and (i!=g) and (i!=o) and (i!=n) and (i!=e) and (i!=l) and (i!=f):
                                                            for c in range (0,10):
                                                                if (c!=s) and (c!=a) and (c!=g) and (c!=o) and (c!=n) and (c!=e) and (c!=l) and (c!=i) and (c!=f):
                                                                    slovo1 = s*1000 + a*100 + g*10 + o
                                                                    slovo2 = s*1000 + a*100 + n*10 + o
                                                                    slovo3 = f*10000 + e*1000 + l*100 + i*10 + c
                                                                    if ((slovo1 + slovo2) == slovo3):
                                                                        pocet=pocet+1
                                                                        print("Riešenie č. ", pocet, ":")
                                                                        print(' S=',s,', A=',a,', G=',g,', O=',o,', N=',n,', F=',f,', E=',e,', L=',l,', I=',i,', C=',c)
                                                                        print("-----> ",s,a,g,o, "+",s,a,n,o, "=",f,e,l,i,c)
print("Úloha má", pocet, "riešení.")                                                                        
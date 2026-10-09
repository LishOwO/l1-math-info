def etoile():
    print('*', end='')
    
def diese():
    print('#', end='')
    
def nouvelle_ligne():
    print()
    
def tapis_a(l, h):
    
    i = 0
    j = 0
    
    while i < h:
        while j < l:
            etoile()
            j += 1
        nouvelle_ligne()
        i += 1
        j = 0
        
tapis_a(10, 10)
nouvelle_ligne()

def tapis_b(l, h):
    
    i = 0
    j = 0
    
    while i < h:
        while j < l:
            if j%2 == 1:
                diese()
            else:
                etoile()
            j += 1
        nouvelle_ligne()
        i += 1
        j = 0
        
tapis_b(10, 10)
nouvelle_ligne()

def tapis_c(l, h):
    i = 0
    j = 0
    
    while i < h:
        while j < l:
            if i%2 == 0:
                if j%2 == 0:
                    etoile()
                else:
                    diese()
            else:
                if j%2 == 0:
                    diese()
                else:
                    etoile()
            j += 1
        nouvelle_ligne()
        i += 1
        j = 0


tapis_c(10, 10)
nouvelle_ligne()


def tapis_d(l, h):
    i = 0
    j = 0
    
    while i < h:
        while j < l:
            if i%3 == 0:
                if j%2 == 0:
                    etoile()
                else:
                    diese()
            elif i%3 == 1:
                if j%2 == 0:
                    diese()
                else:
                    etoile()
            else:
                etoile()
            j += 1
        nouvelle_ligne()
        i += 1
        j = 0

tapis_d(10, 10)
nouvelle_ligne()

def ligne(symb1, symb2, n):
    i = 0
    while i<n:
        if i%2 == 0:
            symb1()
        else :
            symb2()
        i=i+1
    nouvelle_ligne()
    
    
ligne(etoile,diese,10)
ligne(diese,etoile,10)
ligne(etoile,etoile,10)


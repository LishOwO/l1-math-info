def etoile():
    print('*', end='')
    
def diese():
    print('#', end='')
    
def nouvelle_ligne():
    print()

def barre_1():
    print('/', end='')
    
def barre_2():
    print('\\', end='')
    
def tapis_e(l, h):
    
    i = 0
    j = 0
    
    while i < h:
        while j < l:
            if i == 0 or i == h-1:
                etoile()
            elif j == 0 or j == l-1:
                etoile()
            else:
                diese()
            j += 1
        nouvelle_ligne()
        i += 1
        j = 0
    
tapis_e(10, 10)
nouvelle_ligne()

def tapis_f(l, h):
    i = 0
    j = 0
    
    while i < h:
        while j < l:
            if j == h - i - 1:
                etoile()
            else:
                diese()
            j += 1
        nouvelle_ligne()
        i += 1
        j = 0
        
tapis_f(10, 10)
nouvelle_ligne()


def tapis_g(l, h):
    
    assert l%2 == 0, "l doit être pair"
    
    i = 0
    j = 0

    
    while i < h:
        while j < l:
            if j == h - i - 1:
                etoile()
            else:
                diese()
            j += 1
        nouvelle_ligne()
        i += 1
        j = 0
        
def tapis_h(l, h):
    assert l % 2 == 0, "l doit être pair"
    
    i = 0
    j = 0
    
    while i < h:
        while j < l:
            
            if i < h // 2: #si on est dans la moitié haute du tapis
                if j == (l // 2) - 1 - i:
                    barre_1()
                elif j == (l // 2) + i:
                    barre_2()
                else:
                    diese()
                    
            else: #si on est dans la moitié basse du tapis, inverse de haut
                i_bas = h - 1 - i
                if j == (l // 2) - 1 - i_bas:
                    barre_2()
                elif j == (l // 2) + i_bas:
                    barre_1()
                else:
                    diese()
            j += 1
        nouvelle_ligne()
        i += 1
        j = 0
        
tapis_h(10, 10)
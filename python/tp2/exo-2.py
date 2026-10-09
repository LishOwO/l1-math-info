def suivant(u):
    
    assert u > 0, "Le nombre doit être positif"
    
    if u%2 == 0:
        return u//2
    else:
        return 3*u + 1

assert suivant(12) == 6
assert suivant(3) == 10
assert suivant(16) == 8
assert suivant(5) == 16

def syracuse(u):
    nombre = u
    while nombre != 1:
        print(nombre, end=' -> ')
        nombre = suivant(nombre)
    print(1)
    
def nombre_syracuse(u):
    nombre = u
    i = 0
    while nombre != 1 :
        nombre = suivant(nombre)
        i += 1
    return i

assert nombre_syracuse(1) == 0
assert nombre_syracuse(2) == 1
assert nombre_syracuse(5) == 5
assert nombre_syracuse(12) == 9

def plus_grand_syracuse(u):
    i = 1
    max_ = 1
    while i <= u:
        if nombre_syracuse(i) > nombre_syracuse(max_):
            max_ = i
        i+=1
    return max_

assert plus_grand_syracuse(100) = 97

syracuse(12)
    
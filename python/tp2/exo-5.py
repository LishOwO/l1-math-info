def deriver(f, a, h):
    return (f(a + h) - f(a)) / h


def resoudre(f, a0, h):
    a = a0
    
    while abs(f(a)) >= h:
        f_prime_a = deriver(f, a, h)
        a = a - f(a) / f_prime_a
        
    return a

def f(x):
    return x**2 - 2

a0 = 1
h = 1e-6

def g(x):
    return x**2 - 3


racine_2 = resoudre(f, a0, h)
print(racine_2)

racine_3 = resoudre(g, a0, h)
print(racine_3)
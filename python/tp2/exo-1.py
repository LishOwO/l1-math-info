def fac_rec(n):
    if n == 0:
        return 1
    else:
        return (n * fac_rec(n-1))

def fac(n):
    i=1
    resultat=1
    while i<=n:
        resultat = resultat * i
        i+=1
    return resultat


assert fac(5) == 120
assert fac_rec(5) == 120
assert fac(0) == 1
assert fac_rec(0) == 1
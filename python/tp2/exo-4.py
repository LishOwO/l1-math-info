def fermat(n):
    return 2**(2**n) + 1

assert fermat(2) == 17
assert fermat(3) == 257

def premier_facteur(n):
    assert n > 1, "Le nombre doit être supérieur à 1"
    i = 2
    while i<=n:
        if n%i == 0:
            return i
        i += 1

assert premier_facteur(35) == 5
assert premier_facteur(31) == 31
assert premier_facteur(5) == 5
assert premier_facteur(8) == 2

def fermat_premier():
    n = 1
    while premier_facteur(fermat(n)) == fermat(n):
        n+=1
    print(f"Le premier nombre de fermat non-premier est n={n}")

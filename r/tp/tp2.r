Somme2Max <- function(x,y,z){
    if (y >= x && z >= x) return(y + z)
    if (x >= y && z >= y) return(x + z)
    if (x >= z && y >= z) return(x + x)
}

Somme2Max2 <- function(x,y,z){
  if (max(x,y,z) == x){
    return(x + max(y,z))
  } else if (max(x,y,z) == y){
    return(y + max(x,z))
  } else return(z + max(x,y))
}

Somme2Max3 <- function(x,y,z){
  return(x+y+z - min(x,y,z))
}

PrintSomme2Max <- function(x,y,z){
  resultat <- Somme2Max(x,y,z)
  cat("Le résultat de l'appel de fonction Somme2Max(",x,",",y,",",z,") est ",resultat, ".\n", sep = "")
}

RandPair <- function(n) {
  borneSup <- n %/% 2
  return(2 * sample(0:borneSup, size = 1))
}

MonteCarlo <- function() return(sample(c(2, 3, 5), size = 1))

LasVegas <- function() return(sample(c(2, 3, 5), size = 1, prob(1, 2, 3)))

#table(replicate(1000, LasVegas())) permet de faire 1000 fois l'experience LasVegas

RandChiffres <- function(n){
  borneInf <- 10 ** (n-1)
  borneSup <- 10 ** n - 1
  return(sample(borneInf:borneSup, size = 1))
}

Serie <- function(r1, r2){
  return (r1 + r2)
}

Parallele <- function(r1, r2){
  return(1/(1/r1 + 1/r2))
}

Circuit1 <- function(r1, r2, r3){
  return (Serie(r1, Parallele(r2, r3)))
}

Circuit2 <- function(r1, r2, r3){
  return (Serie(Parallele(Parallele(r1, r2), r3), Parallele(r2, r3)))
}

hconv <- function(s){
  secondes <- s%%60
  reste <- s - secondes
  minutes <- (reste) %/% 60 %% 60
  reste <- s - minutes*60
  heures <- reste %/% 3600
  cat(heures, minutes, secondes,"\n", sep=":")
}

Tranche <- function(s, b, h, p){
  if (s - b <= 0) return(0)
  else if (h == -1) return((s - b) * p / 100)
  else if (s >= h) return((h - b) * p / 100)
  else return((s - b) * p / 100)
}

Impot <- function(s){
  total <- Tranche(s, 8000, 25000, 10) + Tranche(s, 25000, -1, 20)
  return(floor(total * 100) / 100)
}

CalculerNoteFinale <- function(ct1, ct2, cp, ca1, ca2){
  NC <- (max(cp, ct1) + (ca1 + ca2)/2)/2
  N1 <- max(ct1, 0.4*NC + 0.6*ct1)
  N2 <- max(N1, ct2, 0.2*NC + 0.8*ct2)
  return(N2)
}

CalculerHypotenuse <- function(){
  cat("Longueur de a:")
  a <- scan()
  cat("Longueur de b:")
  b <- scan()
  return((a**2 + b**2)**(1/2))
}


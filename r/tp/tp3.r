FactRec <- function(n){
  if (n == 0) return (1)
  if (n == 1) return (1)
  return (n * FactRec(n-1))
}

Fact <- function(n){
  resultat <- 1
  i <- 1
  while (i <= n){
    resultat <- resultat * i
    i <- i + 1
  }
  return (resultat)
}

AfficherFact <- function(){
  for(i in 1:10){
    cat(Fact(i), "\n")
  }
}

AfficherFactEffi <- function(){
  resultat <- 1
  for(i in 1:10){
    resultat <- resultat * i
    cat(resultat, "\n")
    
  }
}

SomCh <- function(n){
  somme <- 0
  nombre <- n
  while(n > 0){
    somme <- somme + n%%10
    n <- n %/% 10
  }
  return(somme)
}

ConversionBase <- function(n, b){
  resultat <- 0
  i = 0
  while (n>0){
    resultat <- resultat + (n%%b) * (10**i)
    n <- n%/%b
    i <- i+1
  }
  return (resultat)
}

SomChBin <- function(n){
  bin_ <- ConversionBase(n, 2)
  somme <- 0
  while(bin_ > 0){
    somme <- somme + bin_%%10
    bin_ <- bin_ %/% 10
  }
  return(somme)
}
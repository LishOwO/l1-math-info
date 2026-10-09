MaximizeConvTries <- function(n) {
    return(c(0, 0))
}

MaxTransf <- function(n) {
  points_restant <- n

  for (nb_transf in (points_restant %/% 7):0) {
    
    points_restant1 <- points_restant - 7 * nb_transf
    
    if (points_restant1 %% 3 == 0) return(c(nb_transf, 0))
    
    for (nb_essai in (points_restant1 %/% 5):0){
      
      points_restant2 <- points_restant1 - 5 * nb_essai
      
      if (points_restant2 %% 3 == 0) return(c(nb_transf, nb_essai))
    }
  }
  return(c(0, 0))
}

MaxTranfOpti <- function(n) {
  points <- n
  resultat <- c(0, 0)
  
  if (points == 5) return (c(0, 1))
  if (points < 7) return (c(0, 0))
  if (points%%7 == 0) return (c((n%/%7), 0))
  
  ajout <- c(((n %/% 7)-1), 0)
  restant <- points%%7
  possibilite <- list(c(0,1), c(0,0) ,c(1,0) ,c(0,1) ,c(1,1), c(1,0))
  return(possibilite[[restant]] + ajout)
}
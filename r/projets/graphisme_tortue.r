library("TurtleGraphics")
turtle_init()
turtle_hide()

Oursin <- function(epine, longueur){
  angle <- 1 / epine
  longueur_epine <- runif(epine, min = 0, max = longueur)
  colors <- rainbow(epine)
  for (i in seq_along(longueur_epine)) {
    turtle_col(colors[i])
    turtle_forward(longueur_epine[i])
    turtle_forward(-longueur_epine[i])
    turtle_right(angle)
  }

}



Oursin(100,50);
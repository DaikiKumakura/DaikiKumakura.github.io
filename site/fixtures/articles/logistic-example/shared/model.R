time <- seq(0, 20, by = 0.1)
r <- 0.4
K <- 100
N0 <- 5
N <- K / (1 + ((K - N0) / N0) * exp(-r * time))
plot(time, N, type = "l", xlab = "Time", ylab = "Population size")

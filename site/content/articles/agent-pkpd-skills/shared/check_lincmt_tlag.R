suppressMessages(library(rxode2))
m1 <- rxode2({ ka <- 1; cl <- 0.13; v <- 8; tlag <- 2; cp <- linCmt() })
m2 <- rxode2({ ka <- 1; cl <- 0.13; v <- 8; cp <- linCmt() })
m3 <- rxode2({ ka <- 1; cl <- 0.13; v <- 8; alag(depot) <- 2; cp <- linCmt() })
ev <- et(amt = 100) |> et(seq(0.5, 6, by = 0.5))
a <- rxSolve(m1, ev)$cp; b <- rxSolve(m2, ev)$cp; c <- rxSolve(m3, ev)$cp
cat("tlag variable ignored:", isTRUE(all.equal(a, b)), " alag changes:", !isTRUE(all.equal(b, c)), "\n")

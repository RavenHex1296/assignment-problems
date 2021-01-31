squareSingleDigitNumbers n = filter ( < 100) (map (^2) n)

main = print (squareSingleDigitNumbers [2, 7, 15, 11, 5])
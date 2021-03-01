letterToNumber n
    |n == "F" = 0
    |n == "D" = 1
    |n == "C" = 2
    |n == "B" = 3
    |n == "A" = 4

division a b = (fromIntegral a) / (fromIntegral b)

calcGPA n = division (sum (map (letterToNumber) (n)))  ((length n))


main = print(calcGPA(["A", "B", "B", "C", "C", "C", "D", "F"]))



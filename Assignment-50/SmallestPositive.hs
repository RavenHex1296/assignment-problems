findSmallestPositive :: (Num a, Ord a) => [a] -> a
findSmallestPositive [] = error "smallest positive of empty list"  
findSmallestPositive [x] = x
findSmallestPositive (x:xs)
    | (x < minTail) && (x > 0) = x
    | otherwise = minTail
    where minTail = findSmallestPositive xs

main = print (findSmallestPositive [8, 3, -1, 2, -5, 7])

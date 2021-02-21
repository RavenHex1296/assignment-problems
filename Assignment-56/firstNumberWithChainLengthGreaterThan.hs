chain :: (Integral a) => a -> [a]  
chain 1 = [1]  
chain n  
    | even n =  n:chain (n `div` 2)  
    | odd n  =  n:chain (n*3 + 1)

chainlength = length . chain
exceedlength n = takeWhile (<n) (map (chainlength) [1..])
firstNumberWithChainLengthAtLeast n = length (exceedlength n) + 1

main = print (firstNumberWithChainLengthAtLeast 15)
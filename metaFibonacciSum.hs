fib :: (Integral a) => a -> a  
fib 0 = 0
fib 1 = 1 
fib n = (fib (n - 2)) + (fib (n - 1))

sequenceTerms k = [fib n | n <- [0..k]]
partialSum = sum . sequenceTerms 
metaSumEntries n = [partialSum n | n <- sequenceTerms n]
metaSum = sum . metaSumEntries

main = print (metaSum 6)
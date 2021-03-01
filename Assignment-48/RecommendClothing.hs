recommendClothing :: (RealFloat a) => a -> a -> String  
recommendClothing degreesCelsius  
    | degreesFahrenheit  >= 80 = "Wear a shortsleeve shirt"
    | degreesFahrenheit  > 65 = "Wear a longsleeve shirt"
    | degreesFahrenheit  > 50 = "Wear a sweater"
    | degreesFahrenheit  <= 50 = "Wear a jacket"
    where degreesFahrenheit  = degreesCelsius * 9/5 + 32 

main = print (recommendClothing 5)
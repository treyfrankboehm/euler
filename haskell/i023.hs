upper = 28123

divIntTwo :: (Integral a) => a -> a
divIntTwo n = ceiling(fromIntegral(n)/2)

propDivisors :: (Integral a) => a -> [a]
propDivisors 1 = [1]
propDivisors n = [x | x <- [1..divIntTwo(n)], mod n x == 0]

isAbundant :: Integer -> Bool
isAbundant n
    | odd n = False
    | n >= sum (propDivisors n) = True
    | otherwise = False

abundant = [x | x <- [1..upper], isAbundant x]

solution = length abundant

main = do print abundant


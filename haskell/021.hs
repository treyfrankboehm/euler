divIntTwo :: (Integral a) => a -> a
divIntTwo n = ceiling(fromIntegral(n)/2)

propDivisors :: (Integral a) => a -> [a]
propDivisors 1 = [1]
propDivisors n = [x | x <- [1..divIntTwo(n)], mod n x == 0]

isAmicable :: Integer -> Bool
isAmicable n
    | n == sum (propDivisors (sum (propDivisors n))) && n /= sum (propDivisors n) = True
    | otherwise = False

amicablePairs = [x | x <- [1..10000], isAmicable x]

solution = sum amicablePairs

main = do print solution

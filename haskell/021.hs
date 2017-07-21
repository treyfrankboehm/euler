divIntTwo :: (Integral a) => a -> a
divIntTwo n = floor(fromIntegral(n)/2)

propDivisors :: (Integral a) => a -> [a]
propDivisors 1 = [1]
propDivisors n = [x | x <- [1..divIntTwo(n)], mod n x == 0]

isAmicable :: Integer -> Bool
isAmicable n
    | odd n = False
    | n == sum (propDivisors (sum (propDivisors n))) && n /= sum (propDivisors n) = True
    | otherwise = False

amicablePairs = [x | x <- [1..10000], isAmicable x]

solution = sum amicablePairs

main = do print solution


isPrime :: Integer -> Bool
isPrime 0 = False
isPrime 1 = False
isPrime 2 = True
isPrime n
    | sum [x | x <- [2..rupSqrt n], mod n x == 0] == 0 = True
    | otherwise = False

rupSqrt :: Integer -> Integer
rupSqrt n = ceiling(sqrt(fromInteger(n)))

testNum = 600851475143

factors = [x | x <- [2..rupSqrt testNum], mod testNum x == 0]
primeFactors = [x | x <- factors, isPrime x]
solution = last primeFactors

main = do print solution


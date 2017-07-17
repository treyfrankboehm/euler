rupSqrt :: Integer -> Integer
rupSqrt n = ceiling(sqrt(fromInteger(n)))

isPrime :: Integer -> Bool
isPrime 0 = False
isPrime 1 = False
isPrime 2 = True
isPrime n
    | sum [x | x <- [2..rupSqrt n], mod n x == 0] == 0 = True
    | otherwise = False

primes = [x | x <- [1..], isPrime x]
main = do print (last (take 10001 primes))

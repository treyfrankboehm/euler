-- This is very slow. How to implement a prime sieve in Haskell?!
isPrime :: Integer -> Bool
isPrime 0 = False
isPrime 1 = False
isPrime 2 = True
isPrime n
    | sum [x | x <- [2..rupSqrt n], mod n x == 0] == 0 = True
    | otherwise = False

rupSqrt :: Integer -> Integer
rupSqrt n = ceiling(sqrt(fromInteger(n)))

primes = [x | x <- [2..], isPrime x]
firstTwoMillion = sum (take 2000000 primes)

main = do print firstTwoMillion

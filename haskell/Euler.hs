module Euler where

-- Number of Collatz steps to take n to 1
collatz :: Integral a => a -> a
collatz n
    | n == 1 = 1
    | even n = 1 + collatz(div n 2)
    |  odd n = 1 + collatz(3*n+1)

-- Break an integer up into its digits in a list
listify :: Integral a => a -> [a]
listify n
    | n < 10 = [n]
    | n >= 10 = listify (div n 10) ++ [mod n 10]

-- If a list of digits is the same as its reverse, it's a palindrome
isPal :: Int -> Bool
isPal n = listify n == reverse (listify n)

-- Return True if a number is prime, otherwise false
isPrime :: Integer -> Bool
isPrime 0 = False
isPrime 1 = False
isPrime 2 = True
isPrime n
    | sum [x | x <- [2..rupSqrt n], mod n x == 0] == 0 = True
    | otherwise = False

-- Round-up square root of a number
rupSqrt :: Integer -> Integer
rupSqrt n = ceiling(sqrt(fromInteger(n)))


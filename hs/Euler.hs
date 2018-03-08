module Euler where

-- Number of Collatz steps to take n to 1
collatz :: Integral a => a -> a
collatz n
    | n == 1 = 1
    | even n = 1 + collatz(div n 2)
    |  odd n = 1 + collatz(3*n+1)

concatnums :: Integral a => a -> a -> [a]
concatnums a b = concat [listify a, listify b]

-- An (unsorted) list of a number's divisors. First grab all the pairs
-- by looking at x and n/x up to the square root of n. Then look at the
-- square root itself and add that on if it is a factor (if the number
-- is a actually a square). This avoids double-counting factors.
divisors :: Integral a => a -> [a]
divisors n = concat [ [x, n `div` x]
                      | x <- [1..rupSqrt(n)-1], mod n x == 0]
                      ++ [rupSqrt n | isSquare n]

-- Basic recursive definition of factorial
factorial :: Integral a => a -> a
factorial 0 = 1
factorial n = n * factorial (n-1)

-- Break an integer up into its digits in a list
listify :: Integral a => a -> [a]
listify n
    | n < 10 = [n]
    | n >= 10 = listify (div n 10) ++ [mod n 10]

-- Combinations, n `choose` k
choose :: Integral a => a -> a-> a
choose n k = factorial n `div` (factorial k * factorial (n-k))

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

-- Test whether a number is a square
isSquare :: Integral a => a -> Bool
isSquare n = (rupSqrt n)^2 == n

-- Round-down square root of an int
rdnSqrt :: Integral a => a -> a
rdnSqrt n = floor $ sqrt $ fromIntegral n

-- Round-up square root of an int
rupSqrt :: Integral a => a -> a
rupSqrt n = ceiling $ sqrt $ fromIntegral n

-- The nth triangular number
triangular :: Integral a => a -> a
triangular n = div (n*(n+1)) 2


-- Break an integer up into its digits in a list
listify :: Integral a => a -> [a]
listify n
    | n < 10 = [n]
    | n >= 10 = listify (div n 10) ++ [mod n 10]

-- If a list of digits is the same as its reverse, it's a palindrome
isPal :: Int -> Bool
isPal n = listify n == reverse (listify n)

-- Palindromes of products of 3-digit numbers (m < n to avoid doubles)
pals = [m*n | m <- [100..999], n <- [100..999], m < n, isPal $ m*n]

solution = maximum pals

main = do print solution


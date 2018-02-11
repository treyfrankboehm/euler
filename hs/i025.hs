digits :: Integer -> Integer
digits n
    | n < 10 = 1
    | otherwise = 1 + digits (div n 10)

fibs = 0 : 1 : zipWith (+) fibs (tail fibs)
-- This gets my the NUMBER, not the index of that number.
solution = head [x | x <- fibs, digits x >= 10]

main = do print solution


triangle :: (Integral a) => a -> a
triangle 1 = 1
triangle n = n + triangle (n-1)

divIntTwo :: (Integral a) => a -> a
divIntTwo n = ceiling(fromIntegral(n)/2)

divisors :: (Integral a) => a -> [a]
divisors 1 = [1]
divisors n = [x | x <- [1..divIntTwo(n)], mod n x == 0] ++ [n]

triangulars = map triangle [1..]

solution = head [x | x <- triangulars, length (divisors x) >= 500]

main = do print solution

isPtriple :: (Integral a) => (a, a, a) -> Bool
isPtriple (a, b, c)
    | c < a || c < b || b < a = False -- Avoid double counting
    | a^2 + b^2 == c^2 = True
    | otherwise = False

rupSqrt :: Integer -> Integer
rupSqrt n = ceiling(sqrt(fromInteger(n)))

-- Because a and b must be less than c, we can set an upper bound
upper = 500

triplets = [(a, b, rupSqrt (a^2+b^2)) | a <- [1..upper], b <- [1..upper]]
triples = filter isPtriple triplets
solution = head [a*b*c | (a, b, c) <- triples, a+b+c == 1000]

main = do print solution

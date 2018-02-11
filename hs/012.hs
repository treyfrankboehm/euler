import Euler -- divisors, triangular

numDivisors = [(n, length $ divisors n) | n <- map triangular [1..]]

solution = fst $ [(x, l) | (x, l) <- numDivisors, l >= 500] !! 0

main = do print solution


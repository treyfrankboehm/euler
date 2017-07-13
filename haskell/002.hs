fibs = 0 : 1 : zipWith (+) fibs (tail fibs)
-- 1000 should be enough...
solution = sum (filter even [x | x <- take 1000 fibs, x < 4000000])

main = do print solution

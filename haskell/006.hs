sumSquare :: Integer -> Integer
sumSquare n = sum [x^2 | x <- [1..n]]

squareSum :: Integer -> Integer
squareSum n = (sum [1..n])^2

upper = 100
solution = (squareSum upper) - (sumSquare upper)

main = do print solution


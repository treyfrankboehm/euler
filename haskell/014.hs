collatz :: Integer -> Integer
collatz n
    | n == 1 = 1
    | even n = 1 + collatz(toInteger(ceiling(fromInteger(n)/2)))
    |  odd n = 1 + collatz(3*n+1)

chains = [(num, collatz num) | num <- [1..1000]]

-- Need to find the maximum collatz num and print the num


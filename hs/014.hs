collatz :: Integral a => a -> a
collatz n
    | n == 1 = 1
    | even n = 1 + collatz(div n 2)
    |  odd n = 1 + collatz(3*n+1)

chains = [(num, collatz num) | num <- [1..1000000]]
highestChain = maximum ([chain | (num, chain) <- chains])
solution = [num | (num, chain) <- chains, chain == highestChain] !! 0

main = do print solution


-- No programming required here. Smallest num evenly divisible by 1..20:
-- 1) Get prime factors of 1 through 20
-- 2) Multiply them all together
-- 1*2*3*2*5*7*2*3*11*13*2*17*19 = (2^4)*(3^2)*5*7*11*13*17*19

solution = (2^4)*(3^2)*5*7*11*13*17*19

main = do print solution

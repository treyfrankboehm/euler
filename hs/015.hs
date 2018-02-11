-- No programming required. This is a simple discrete math problem that
-- involves counting binary strings. Let 1 indicate a move to the right
-- and 0 indicate a move to the left. How many binary strings of length
-- 40 with exactly 20 ones? 40 choose 20.

import Euler -- combinations

solution = 40 `choose` 20

main = do print solution


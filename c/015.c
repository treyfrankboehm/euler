#include <stdio.h>
#include "Euler.h"

int main(void)
{
    /* I had this problem in discrete math. It is equivalent to asking:
     * How many binary strings with length 40 containing exactly 20 1s
     * are there? This is answered with a binomial coefficient:
     *  nChooseK(40, 20)
     * Unfortunately, 40! is way too large to fit in a uint64_t, so I
     * will need to use a big int library (like gmp) or do some clever
     * simplifications to make this work. I know the answer 137846528820
     * can fit in 37 bits, but would rather not include a bunch of
     * dividing-down by hand.
     */
    return 0;
}

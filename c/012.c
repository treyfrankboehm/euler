#include <stdio.h>
#include "Euler.h"

int main(void)
{
    int n, num, factor_count;
    int step = 1;
    for (num = 1; numFactors(num) < 500; num += step) {
        step++;
    }
    printf("%d\n", num);
    return 0;
}


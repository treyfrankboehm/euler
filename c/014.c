#include <stdio.h>
#include <stdint.h>
#include "Euler.h"

int main(void)
{
    uint64_t num;
    int chain;
    int max_starting = 1;
    int max = 0;
    for (num = 1; num < 1e6; num++) {
        chain = collatz(num);
        if (chain > max) {
            max_starting = num;
            max = chain;
        }
    }
    printf("%d\n", max_starting);
    return 0;
}

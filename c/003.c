#include <stdio.h>
#include <math.h>
#include "Euler.h"

int main(void) {
    uint64_t num = 600851475143;
    uint64_t num_sqrt = (uint64_t)sqrt(num);
    uint64_t factor, cofactor;
    uint64_t largest = 0;
    for (factor = 2; factor < num_sqrt; factor++) {
        if (num % factor)
            continue; // not a factor
        cofactor = num/factor;
        if (factor > largest && isPrime(factor)) {
            largest = factor;
        }
        if (cofactor > largest && isPrime(cofactor)) {
            largest = cofactor;
        }
    }
    printf("%lu\n", largest);
    return 0;
}


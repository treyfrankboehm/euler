#include <stdio.h>
#include <stdint.h>
#include "Euler.h"

/* Find all primes under 2,000,000 */
#define UPPER_LIMIT 2000000

/* Assume that every integer is prime until shown otherwise. */
uint8_t Factorable[UPPER_LIMIT] = {0};

int main(void)
{
    uint32_t i;
    uint64_t sum = 0;
    sieve(Factorable, UPPER_LIMIT);
    for (i = 0; i < UPPER_LIMIT; i++) {
        if (!Factorable[i]) {
            sum += i;
        }
    }
    printf("%lu\n", sum);
    return 0;
}


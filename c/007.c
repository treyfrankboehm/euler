#include <stdio.h>
#include <stdint.h>
#include "Euler.h"

/* The prime number theorem tells us that there are roughly N/log(N)
 * prime numbers below N. Setting N/log(N) equal to 10001 (to find the
 * 10001st prime) yields roughly 120,000. We'll go with a nice round
 * power of 2 (2^17) for our upper limit for the sieve.
 */

#define UPPER_LIMIT (1 << 17)

/* Assume that every integer is prime until shown otherwise. */
uint8_t Factorable[UPPER_LIMIT] = {0};

int main(void)
{
    uint32_t i;
    uint32_t count = 0;
    sieve(Factorable, UPPER_LIMIT);
    for (i = 0; i < UPPER_LIMIT; i++) {
        if (!Factorable[i]) {
            count++;
        }
        if (count == 10001) {
            printf("%d\n", i);
            break;
        }
    }
    return 0;
}


#include <stdio.h>
#include <stdint.h>
#include <math.h>
#include "Euler.h"

int isAbundant(int num)
{
    return (num < sumFactor(num));
}

int sumFactor(int num)
{
    int sum = 1;
    int factor, cofactor;
    for (factor = 2; factor <= sqrt(num); factor++) {
        if (num % factor == 0) {
            cofactor = num / factor;
            sum += factor;
            /* Add on the complement unless it's a square root */
            if (cofactor != factor) {
                sum += cofactor;
            }
        }
    }
    return sum;
}

/* sieve: Create an array that has a 0 at every prime index, and a 1 at
 * every composite (factorable) index. Parameters are an array of ints
 * (called "factorable") that has been initialized to 0, and the length
 * of that array (called "upper_limit")
 */
void sieve(uint8_t* factorable, uint32_t upper_limit)
{
    int i, j;
    factorable[0] = 1;
    factorable[1] = 1;
    for (i = 2; i < upper_limit; i++) {
        for (j = 2*i; j < upper_limit; j += i) {
            factorable[j] = 1;
        }
    }
}


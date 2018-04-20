#include <stdio.h>
#include "Euler.h"

int main(void)
{
    /* Smallest number that is a product of two 3-digit numbers: 10000
     * Largest number that is a product of two 3-digit numbers: 998001
     */
    int lower = 10000;
    int upper = 998001;
    int a, b, product;

    /* Start with the highest possible product and work down */
    for (product = upper; product >= lower; product--) {
        /* If it isn't a palindrome, go on to the next candidate */
        if (!isPalindrome(product)) { continue; }

        /* If it is a palindrome, try to factor it */
        for (a = 999; a >= 100; a--) {
            b = product / a;
            /* b must 1) Be a factor, and 2) Have 3 digits */
            if ((a*b == product) && (numDigits(b) == 3)) {
                printf("%d\n", product);
                return 0;
            }
        }
    }
    return 1;
}


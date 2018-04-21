#include <stdio.h>

int main(void)
{
    /* The smallest number divisible by all numbers 1-20 means that each
     * of those numbers will be contained in the factorization.
     * The prime numbers under 20 are 2, 3, 5, 7, 11, 13, 17, and 19.
     * The number with the most 2s in its prime factorization is 16: 2^4
     * The number with the most 3s in its prime factorization is 9: 3^2
     * No number has more than 1 of each of the other prime factors.
     * So, the number is just:
     */
    printf("%d\n", 2*2*2*2*3*3*5*7*11*13*17*19);
    return 0;
}

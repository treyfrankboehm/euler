#include <stdio.h>
#include <stdint.h>
#include <math.h>
#include <gmp.h>
#include "Euler.h"

/* collatz: Return the number of terms in the Collatz sequence for num */
int collatz(uint64_t num)
{
    int count = 1;
    while (num > 1) {
        if (num % 2) {
            num = 3*num+1;
        } else {
            num = num/2;
        }
        count++;
    }
    return count;
}

/* factorial: Return num! (calculate iteratively to save stack frames.
 * Only works for num in {0..20} because of size limitations.
 */
uint64_t factorial(int num)
{
    uint64_t f = 1;
    for ( ; num > 0; num--) {
        f *= num;
    }
    return f;
}

/* isAbundant: Test if the number is abundant (the sum of the factors is
 * greater than the number itself)
 */
int isAbundant(int num)
{
    return (num < sumFactor(num));
}

/* isPalindrome: Test if the number is a palindrome in decimal */
int isPalindrome(int num)
{
    return (num == reverseNum(num));
}

/* nChooseK: Calculate binomial coefficients. Because of integer size
 * limitations, this is only good up to n = 20. I plan on using gmp to
 * extend this and factorial, at some point.
 */
int nChooseK(int n, int k)
{
    if (k > n || n < 0 || k < 0)
        return 0; /* Restrict to 0 <= k <= n */
    return factorial(n)/(factorial(k)*factorial(n-k));
}

/* numDigits: Return the number of digits in an integer */
int numDigits(int num)
{
    int len;
    for (len = 0; num > 0; num /= 10) {
        len++;
    }
    return len;
}

/* numFactors: Return the number of factors for a number */
int numFactors(int num)
{
    int count = 2;
    int factor, cofactor;
    for (factor = 2; factor <= sqrt(num); factor++) {
        if (num % factor == 0) {
            cofactor = num / factor;
            count++;
            /* Add on the complement unless it's a square root */
            if (cofactor != factor) {
                count++;
            }
        }
    }
    return count;
}


/* reverseNum: Reverse the order of the digits in an integer */
int reverseNum(int num)
{
    int num_digits = numDigits(num);
    int reversed_num = 0;
    int digit;
    int i;
    for (i = num_digits-1; i >= 0; i--) {
        digit = num % 10;
        reversed_num += digit*pow(10, i);
        num /= 10;
    }
    return reversed_num;
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

/* sumFactor: Return the sum of the factors of an integer */
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

/* triangular: Return the nth triangular number */
int triangular(int n)
{
    return n*(n+1)/2;
}


#include <stdio.h>
#include <stdint.h>
#include <math.h>
#include "Euler.h"

/* isAbundant: Test if the number is abundant (the sum of the factors is
 * greater than the number itself)
 */
int isAbundant(int num)
{
    return (num < sumFactor(num));
}

/* isPalindrome: Test if the number is a palindrome in decimal */
int isPalindrome(int n)
{
    return (n == reverseNum(n));
}


/* numDigits: Return the number of digits in an integer */
int numDigits(int n)
{
    int len;
    for (len = 0; n > 0; n /= 10) {
        len++;
    }
    return len;
}

/* reverseNum: Reverse the order of the digits in an integer */
int reverseNum(int n)
{
    int num_digits = numDigits(n);
    int reversed_n = 0;
    int digit;
    int i;
    for (i = num_digits-1; i >= 0; i--) {
        digit = n % 10;
        reversed_n += digit*pow(10, i);
        n /= 10;
    }
    return reversed_n;
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


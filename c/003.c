#include <stdio.h>
#include <gmp.h>
#include <math.h>

int isPrime(int number);

int main(void) {
    /*
    mpz_t dividend;
    mpz_t divisor;
    mpq_t quotient;
    mpz_init_set_ui(dividend, 600851475143);
    mpz_init_set_ui(divisor, 2);
    mpq_init(quotient);

    mpz_clear(dividend);
    mpz_clear(divisor);
    mpq_clear(quotient);
    */
    printf("%d\n", isPrime(6857));

    return 0;
}

int isPrime(int number) {
    int i;
    for(i = 2; i <= sqrt(number); i++) {
        if(number % i == 0) {
            return 0;
        }
    }
    return 1;
}


#ifndef __EULER_H__
#define __EULER_H__
#include <stdio.h>
#include <math.h>
#include <stdint.h>
#include <gmp.h>

int collatz(uint64_t num);
uint64_t factorial(int num);
int isAbundant(uint64_t num);
int isPalindrome(uint64_t num);
int isPrime(uint64_t num);
uint64_t nChooseK(int n, int k);
int numDigits(uint64_t num);
int numFactors(uint64_t num);
uint64_t reverseNum(uint64_t num);
void sieve(uint8_t* factorable, uint64_t upper_limit);
uint64_t sumFactor(uint64_t num);

#endif

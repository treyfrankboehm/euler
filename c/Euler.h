#ifndef __EULER_H__
#define __EULER_H__
#include <stdio.h>
#include <math.h>
#include <stdint.h>
#include <gmp.h>

int collatz(uint64_t num);
uint64_t factorial(int num);
int isAbundant(int num);
int isPalindrome(int num);
int nChooseK(int n, int k);
int numDigits(int num);
int numFactors(int num);
int reverseNum(int num);
void sieve(uint8_t* factorable, uint32_t upper_limit);
int sumFactor(int num);
int triangular(int n);

#endif

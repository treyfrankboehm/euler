#ifndef __EULER_H__
#define __EULER_H__
#include <stdio.h>
#include <math.h>
#include <stdint.h>

int isPalindrome(int n);
int isAbundant(int num);
int numDigits(int n);
int reverseNum(int n);
void sieve(uint8_t* factorable, uint32_t upper_limit);
int sumFactor(int num);

#endif

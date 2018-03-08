#ifndef __EULER_H__
#define __EULER_H__
#include <stdio.h>
#include <math.h>
#include <stdint.h>

int isAbundant(int num);
int sumFactor(int num);
void sieve(uint8_t* factorable, uint32_t upper_limit);

#endif

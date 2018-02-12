#include <stdio.h>
#include "Euler.h"

void generateAbundant(void);
void findAbundantSums(void);

int Upper_Limit = 28124;
/* I don't know how many abundant numbers there are, but an obvious upper
 * bound is half of my highest number (only even numbers are abundant).
 */
int Abundant_Numbers[28124/2] = {0};
int Abundant_Count = 0;
/* Mark each number 0 to 28123 as whether it can be written as the sum
 * of two abundant numbers or not.
 */
int Summable[28124] = {0};

int main(void)
{
    int total;
    int i;

    generateAbundant();
    
    findAbundantSums();

    for (i = 0; i < Upper_Limit; i++) {
        /* If we have a 0 in the number's position in Summable, it was
         * not created as a sum. Add it from the total.
         */
        if (!Summable[i]) {
            total += i;
        }
    }

    printf("%d\n", total);
    return 0;
}

void generateAbundant(void)
{
    int num;
    /* 12 is the first abundant number */
    for (num = 12; num < Upper_Limit; num++) {
        if (isAbundant(num)) {
            Abundant_Numbers[Abundant_Count] = num;
            Abundant_Count++;
        }
    }
}

void findAbundantSums(void)
{
    int i, j, num1, num2, sum;
    /* Index i (num1) will consider every abundant number we have */
    for (i = 0; i < Abundant_Count; i++) {
        num1 = Abundant_Numbers[i];
        /* Index j (num2) only looks at abundant numbers >= num1 */
        for (j = i; j < Abundant_Count; j++) {
            num2 = Abundant_Numbers[j];
            sum = num1+num2;
            /* If the sum is within the bounds, mark it as possible */
            if (sum < Upper_Limit) {
                Summable[sum] = 1;
            } else {
                /* Otherwise, break out of j's loop (num2 only grows */
                break;
            }
        }
    }
}


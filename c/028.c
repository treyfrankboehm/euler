#include <stdio.h>

int spiralSum(int side_length);

int main(void)
{
    printf("%d\n", spiralSum(1001));
}

int spiralSum(int side_length)
{
    int sum = 1;
    int step = 2;
    int i = 1;
    for (step = 2; step < side_length; step += 2) {
        /* One way to to this is by using a loop to add each i to the
         * sum one by one, incrementing i each time like this:
         *      for (j = 0; j < 4; j++) {
         *          i += step; sum += i;
         *      }
         * I decided to do the algebra ahead of time:
         *      sum += (i+step) + (i+2*step) + (i+3*step) + (i+4*step)
         * Which can be further simplified.
         */
        sum += 4*i + 10*step;
        i += (4*step);
    }
    return sum;
}


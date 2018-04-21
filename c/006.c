#include <stdio.h>

int sumOfSquares(int upper);
int squareOfSum(int upper);

int main(void)
{
    int max = 100;
    printf("%d\n", (squareOfSum(max) - sumOfSquares(max)));
    return 0;
}

int sumOfSquares(int upper)
{
    int sum = 0;
    int n;
    for (n = 1; n <= upper; n++) {
        sum += (n*n);
    }
    return sum;
}

int squareOfSum(int upper)
{
    int sum = 0;
    int n;
    for (n = 1; n <= upper; n++) {
        sum += n;
    }
    return sum*sum;
}


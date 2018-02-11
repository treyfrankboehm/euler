#include <stdio.h>

int main(void) {
    int prev = 1;
    int curr = 2;
    int next;
    int evenSum = 0;
    while (curr < 4e6) {
        if (curr % 2 == 0) {
            evenSum += curr;
        }
        next = prev+curr;
        prev = curr;
        curr = next;
    }
    printf("%d\n", evenSum);
    return 0;
}

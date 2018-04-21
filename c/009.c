#include <stdio.h>
#include <math.h>

int main(void)
{
    int a, b, c;
    int a_sq, b_sq, c_sq;
    for (a = 1; a < 1000; a++) {
        a_sq = a*a; /* Only do this operation once for each a */
        for (b = 1; b < a; b++) {
            b_sq = b*b;
            c_sq = a_sq + b_sq;
            c = (int)sqrt(c_sq);
            if (c*c != c_sq)
                continue; /* Not a real triple, go to next b */
            if (a + b + c == 1000) {
                printf("%d\n", a*b*c);
                break;
            }
        }
    }
    return 0;
}


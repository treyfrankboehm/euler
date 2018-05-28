#include <stdio.h>
#include <stdlib.h>

int max(int a, int b);
int nextNum(FILE* fp);
int* populate(FILE* fp);
int collapse(int* nums);

/* The height of the triangle is the only parameter we need to know
 * ahead of time. Even this could be calculated from the file, but I
 * feel that's unnecessary.
 */
static unsigned int TRIANGLE_HEIGHT = 100;

int main(void)
{
    FILE* fp = fopen("p067_triangle.txt", "r");
    int* nums = populate(fp);
    fclose(fp);
    printf("%d\n", collapse(nums));
    free(nums);
    return 0;
}

/* max: Return the larger of two integers.
 */
int max(int a, int b)
{
    if (a >= b) return a;
    return b;
}

/* nextNum: Get the next space-separated number from the file.
 */
int nextNum(FILE* fp)
{
    int num = 0;
    char c;
    for (c = fgetc(fp); c != ' ' && c != '\n'; c = fgetc(fp)) {
        num *= 10;
        num += (c - '0');
    }
    return num;
}

/* populate: Put the triangle into a one-dimensional array.
 */
int* populate(FILE* fp)
{
    int entries = TRIANGLE_HEIGHT*(TRIANGLE_HEIGHT+1)/2;
    int* nums = malloc(sizeof(int)*entries);
    int i;
    char c;
    for (i = 0; i < entries; i++) {
        c = fgetc(fp);
        ungetc(c, fp);
        if (c == EOF) {
            break;
        }
        nums[i] = nextNum(fp);
    }
    return nums;
}

/* collapse: Generate the solution by starting at the bottom of the
 * triangle and collapsing it up. Every number requires two comparisons
 * (a max of two operation) so no searching is necessary. This solution
 * scales with size (from problem 18 to 67).
 */
int collapse(int* nums)
{
    /* Start one row from the bottom
     *         o
     *        o o
     *       o o o
     *      o o o o
     *     x o o o o
     *    o o o o o o
     *
     * Move across the row (ie one column at a time). Replace
     * that number max (current+lower left, current+lower right)
     *          1
     *         2 3
     *
     * In this case, 1 would be replaced with 4. Continue up the
     * triangle until only the apex remains.
     */

    int row, col, index;
    int curr, left, right;
    for (row = TRIANGLE_HEIGHT-2; row >= 0; row--) {
        for (col = 0; col <= row; col++) {
            index = row*(row+1)/2+col;
            curr  = nums[index];
            left  = nums[index+row+1];
            right = nums[index+row+2];
            nums[index] = curr + max(left, right);
        }
    }
    return nums[0];
}


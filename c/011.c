#include <stdio.h>
#include <stdint.h>

void initializeGrid(uint8_t* grid);
int maxProduct(uint8_t* grid, uint8_t x, uint8_t y);
int max4(int a, int b, int c, int d);

int main(void)
{
    uint8_t grid[400] = {0};
    uint8_t x, y;
    int product;
    int max = 0;
    initializeGrid(grid);
    for (x = 0; x < 20; x++) {
        for (y = 0; y < 20; y++) {
            product = maxProduct(grid, x, y);
            max = product > max ? product : max;
        }
    }
    printf("%d\n", max);
    return 0;
}

void initializeGrid(uint8_t* grid)
{
    FILE* grid_file = fopen("/home/trey/code/euler/c/grid_011.txt", "r");
    int i;
    char number[4];
    for (i = 0; i < 400; i++) {
        fscanf(grid_file, "%d", number);
        grid[i] = (uint8_t)number[0];
    }
}

int maxProduct(uint8_t* grid, uint8_t x, uint8_t y)
{
    int right_product = 0;
    int down_product = 0;
    int down_right_product = 0;
    int down_left_product = 0;
    if (x <= 16)
        right_product = grid[x+20*y] * grid[x+1+20*y] * grid[x+2+20*y] * grid[x+3+20*y];
    if (x <= 16 && y <= 16)
        down_right_product = grid[x+20*y] * grid[x+1+20*(y+1)] * grid[x+2+20*(y+2)] * grid[x+3+20*(y+3)];
    if (x >= 3 && y <= 16)
        down_left_product = grid[x+20*y] * grid[x-1+20*(y+1)] * grid[x-2+20*(y+2)] * grid[x-3+20*(y+3)];
    if (y <= 16)
        down_product = grid[x+20*y] * grid[x+20*(y+1)] * grid[x+20*(y+2)] * grid[x+20*(y+3)];

    return max4(right_product, down_product, down_right_product, down_left_product);
}

int max4(int a, int b, int c, int d)
{
    if (a > b && a > c && a > d)
        return a;
    if (b > c && b > d)
        return b;
    if (c > d)
        return c;
    return d;
}


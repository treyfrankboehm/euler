#include <stdio.h>
#include <stdint.h>

int main(void)
{
    uint8_t grid[400];
    uint32_t i, j;
    FILE* grid_file = fopen("grid_011.txt", "r");
    char number[1];
    for (i = 0; i < 400; i++) {
        fscanf(grid_file, "%d", number);
        grid[i] = (uint8_t)number[0];
    }
    for (i = 0; i < 20; i++) {
        for (j = 0; j < 20; j++) {
            printf("%d ", grid[20*i+j]);
        }
        printf("\n");
    }
    return 0;
}


#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <stdlib.h>

#define N 20238

char A_1[N][N];

int multiply(char const *row, char *result)
{
    memset(result, 0, N);
    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < N; ++j)
        {
            result[i] ^= row[j] & A_1[j][i];
        }
    }
    return 0;
}

int main()
{
    FILE *f = fopen("inverse", "rb");
    fread(A_1, sizeof(A_1), 1, f);
    fclose(f);

    char input[N + 1];
    char result[N + 1];

    printf("Ready\n");

    while (1)
    {
        scanf("%s", input);
        for (int i = 0; i < N; ++i)
            input[i] -= '0';
        multiply(input, result);
        for (int i = 0; i < N; ++i)
            putchar(result[i] + '0');
        putchar('\n');
    }
}

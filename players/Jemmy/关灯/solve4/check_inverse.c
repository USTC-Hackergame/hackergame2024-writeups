#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <stdlib.h>

#define N 20238
#define M 1963
#define S (N / 149)

char A[N][N];
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
    FILE *f = fopen("matrix2", "rb");
    fread(A, sizeof(A), 1, f);
    fclose(f);

    f = fopen("inverse", "rb");
    fread(A_1, sizeof(A_1), 1, f);
    fclose(f);

    char result[N];

    for (int i = 0; i < N; ++i)
    {
        printf("Row %d\n", i);
        char const *row = A[i];
        multiply(row, result);
        for (int j = 0; j < N; ++j)
        {
            if (result[j] != (i == j))
            {
                printf("Failed at %d %d\n", i, j);
                return 1;
            }
        }
    }
}

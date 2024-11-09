#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <stdlib.h>

#define N 20238
#define M 1963
#define S (N / 149)

char A[N][N];
char A_1[N][N];

void print_matrix()
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            printf("%d ", A[i][j]);
        }
        printf("        ");
        for (int j = 0; j < N; j++)
        {
            printf("%d ", A_1[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

int inverse()
{
    int i, j, k;
    memset(A_1, 0, sizeof(A_1));
    for (i = 0; i < N; i++)
    {
        A_1[i][i] = 1;
    }

    for (i = 0; i < N; i++)
    {
        if (i % S == 0)
            printf("Stage 1, Layer %d\n", i / S);
        if (A[i][i] == 0)
        {
            for (j = i + 1; j < N; j++)
            {
                if (A[j][i] != 0)
                {
                    for (k = 0; k < N; k++)
                    {
                        A[i][k] ^= A[j][k];
                        A_1[i][k] ^= A_1[j][k];
                    }
                    break;
                }
            }
        }

        if (A[i][i] == 0)
        {
            printf("Invalid pos %d\n", i);
            continue;
        }

        for (j = i + 1; j < N; j++)
        {
            if (A[j][i] != 0)
            {
                for (k = 0; k < N; k++)
                {
                    A[j][k] ^= A[i][k];
                    A_1[j][k] ^= A_1[i][k];
                }
            }
        }
    }

    for (i = N - 1; i >= 0; i--)
    {
        if (i % S == 0)
            printf("Stage 2, Layer %d\n", i / S);
        for (j = i - 1; j >= 0; j--)
        {
            if (A[j][i] != 0)
            {
                for (k = 0; k < N; k++)
                {
                    A[j][k] ^= A[i][k];
                    A_1[j][k] ^= A_1[i][k];
                }
            }
        }
    }
    return 1;
}

int main()
{
    FILE *f = fopen("matrix2", "rb");
    fread(A, sizeof(A), 1, f);
    fclose(f);

    printf("inverse: %d\n", inverse());
    f = fopen("inverse", "wb");
    fwrite(A_1, sizeof(A_1), 1, f);
    fclose(f);
}

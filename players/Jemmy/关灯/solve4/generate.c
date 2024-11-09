#include <stdio.h>
#include <string.h>
#include <assert.h>
#include <stdlib.h>

#define N 149

char mat[3][N][N];
char A[N * N][N * N];
char A_1[N * N][N * N];

void print_matrix()
{
    for (int i = 0; i < N * N; i++)
    {
        for (int j = 0; j < N * N; j++)
        {
            printf("%d ", A[i][j]);
        }
        printf("        ");
        for (int j = 0; j < N * N; j++)
        {
            printf("%d ", A_1[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

int generate(int pos)
{
    memset(mat, 0, sizeof(mat));
    mat[1][pos / N][pos % N] = 1;

    int i0 = 2, i1 = 0, i2 = 1;

    for (int i = 1; i < N + 1; i++)
    {
        i0 = (i0 + 1) % 3;
        i1 = (i1 + 1) % 3;
        i2 = (i2 + 1) % 3;

        memset(mat[i2], 0, sizeof(mat[i2]));

        for (int j = 0; j < N; j++)
        {
            for (int k = 0; k < N; k++)
            {
                mat[i2][j][k] = mat[i1][j][k] ^ mat[i0][j][k];
                if (j > 0)
                    mat[i2][j][k] ^= mat[i1][j - 1][k];
                if (j < N - 1)
                    mat[i2][j][k] ^= mat[i1][j + 1][k];
                if (k > 0)
                    mat[i2][j][k] ^= mat[i1][j][k - 1];
                if (k < N - 1)
                    mat[i2][j][k] ^= mat[i1][j][k + 1];
            }
        }
    }
    return i2;
}

int inverse()
{
    FILE *f = fopen("ignore.txt", "w");
    int i, j, k;
    memset(A_1, 0, sizeof(A_1));
    for (i = 0; i < N * N; i++)
    {
        A_1[i][i] = 1;
    }

    for (i = 0; i < N * N; i++)
    {
        if (i % N == 0)
            printf("Stage 1, Layer %d\n", i / N);
        if (A[i][i] == 0)
        {
            for (j = i + 1; j < N * N; j++)
            {
                if (A[j][i] != 0)
                {
                    for (k = 0; k < N * N; k++)
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
            for (j = 0; j < i; j++)
            {
                if (A[j][i] != 0 && A[j][j] == 0)
                {
                    for (k = 0; k < N * N; k++)
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
            printf("Ignore pos %d\n", i);
            fprintf(f, "%d\n", i);
            fflush(f);
            continue;
        }

        for (j = i + 1; j < N * N; j++)
        {
            if (A[j][i] != 0)
            {
                for (k = 0; k < N * N; k++)
                {
                    A[j][k] ^= A[i][k];
                    A_1[j][k] ^= A_1[i][k];
                }
            }
        }

        for (j = i - 1; j >= 0; j--)
        {
            if (A[j][i] != 0)
            {
                for (k = 0; k < N * N; k++)
                {
                    A[j][k] ^= A[i][k];
                    A_1[j][k] ^= A_1[i][k];
                }
            }
        }
    }
    fclose(f);
    return 0;
}

int main()
{
    for (int i = 0; i < N * N; i++)
    {
        if (i % N == 0)
            printf("Stage 0, Layer %d\n", i / N);
        int res = generate(i);

        memcpy(A[i], mat[res], sizeof(mat[res]));
    }
    FILE *p = fopen("matrix", "wb");
    fwrite(A, sizeof(A), 1, p);
    fclose(p);
    printf("inverse: %d\n", inverse());

    p = fopen("A", "wb");
    fwrite(A, sizeof(A), 1, p);
    fclose(p);

    p = fopen("A_1", "wb");
    fwrite(A_1, sizeof(A_1), 1, p);
    fclose(p);
}

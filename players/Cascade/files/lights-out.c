#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>

typedef struct vector {
    size_t n;
    char* data;
} vector_t;

vector_t vector_new(size_t n) {
    char* data = (char*)malloc(n);
    return (vector_t) {
        .n = n,
        .data = data
    };
}

void vector_erase(vector_t vector) {
    for (size_t i = 0; i < vector.n; i++)
        vector.data[i] = '0';
}

vector_t* vector_new_array(size_t n, size_t count) {
    vector_t* vector_head = (vector_t*)malloc(
        (sizeof(vector_t) * count) + 
        (n * count)
    );
    char* data_head = (char*)(vector_head + count);
    for (size_t i = 0; i < count; i++) {
        vector_t* cur_head = vector_head + i;
        cur_head->n = n;
        cur_head->data = data_head + n * i;
    }
    for (size_t i = 0; i < n * count; i++)
        data_head[i] = '0';
    return vector_head;
}

char char_xor(char a, char b) {
    return (a == b) ? '0' : '1';
};

char char_and(char a, char b) {
    return (a == '1' && b == '1');
};

void vector_xor(vector_t v, vector_t other) {
    for (size_t i = 0; i < v.n; i++)
        v.data[i] = char_xor(v.data[i], other.data[i]);
}

void vector_and(vector_t v, vector_t other) {
    for (size_t i = 0; i < v.n; i++)
        v.data[i] = char_and(v.data[i], other.data[i]);
}

void vector_copy(vector_t dest, vector_t src) {
    for (size_t i = 0; i < dest.n; i++)
        dest.data[i] = src.data[i];
}

void vector_print(vector_t v) {
    putchar('[');
    for (size_t i = 0; i < v.n; i++) {
        putchar(v.data[i]);
    }
    putchar(']');
    putchar('\n');
}

typedef struct matrix {
    size_t row, col;
    vector_t* vectors;
} matrix_t;

matrix_t matrix_new(size_t row, size_t col) {
    vector_t* vectors = vector_new_array(col, row);
    return (matrix_t) {
        .row = row,
        .col = col,
        .vectors = vectors
    };
}

void matrix_print(matrix_t matrix) {
    for (size_t row = 0; row < matrix.row; row++)
        vector_print(matrix.vectors[row]);
}

size_t transform_3d_to_index(int x, int y, int z, int d) {
    return x + (y * d) + (z * d * d);
}

bool in_range(int sign, int l, int r) {
    return (sign >= l && sign < r);
}
bool in_range_3d(int x, int y, int z, int d) {
    return in_range(x, 0, d) && in_range(y, 0, d) && in_range(z, 0, d);
}

void insert_row(matrix_t matrix, vector_t row) {
    for (size_t i = 0; i < matrix.row; i++) {
        if (matrix.vectors[i].data[i] == '1') {
            if (row.data[i] == '1') {
                vector_xor(row, matrix.vectors[i]);
            }
        } else {
            if (row.data[i] == '1') {
                vector_copy(matrix.vectors[i], row);
                return;
            }
        }
    }
}

void eliminate_row(matrix_t matrix, size_t row) {
    for (size_t i = row + 1; i < matrix.row; i++)
        if (matrix.vectors[row].data[i] == '1')
            vector_xor(matrix.vectors[row], matrix.vectors[i]);
}

int main() {
    // generate_data(997, 1000, 114514);
    // return 0;
    // freopen("data", "r", stdin);
    // freopen("out", "w+", stdout);
    fprintf(stderr, "Enter dimensions of lamps and lamps: \n");
    size_t d;
    scanf("%llu", &d);
    size_t size = d * d * d;
    char* lamps = (char*)malloc(size + 4);
    scanf("%s", lamps);

    matrix_t matrix = matrix_new(size, size + 1);
    vector_t vid = vector_new(size + 1);
    for (int z = 0; z < d; z++) {
        for (int y = 0; y < d; y++) {
            for (int x = 0; x < d; x++) {
                vector_erase(vid);
                size_t id = transform_3d_to_index(x, y, z, d);
                vid.data[id] = '1';
                vid.data[size] = lamps[id];
                if (in_range_3d(x - 1, y, z, d))
                    vid.data[transform_3d_to_index(x - 1, y, z, d)] = '1';
                if (in_range_3d(x + 1, y, z, d))
                    vid.data[transform_3d_to_index(x + 1, y, z, d)] = '1';
                if (in_range_3d(x, y - 1, z, d))
                    vid.data[transform_3d_to_index(x, y - 1, z, d)] = '1';
                if (in_range_3d(x, y + 1, z, d))
                    vid.data[transform_3d_to_index(x, y + 1, z, d)] = '1';
                if (in_range_3d(x, y, z - 1, d))
                    vid.data[transform_3d_to_index(x, y, z - 1, d)] = '1';
                if (in_range_3d(x, y, z + 1, d))
                    vid.data[transform_3d_to_index(x, y, z + 1, d)] = '1';
                // vector_print(vid);
                insert_row(matrix, vid);
            }
        }
    }
    // matrix_print(matrix);

    for (size_t i = 0; i < size; i++)
        eliminate_row(matrix, i);
    printf("After elimination:\n");
    // matrix_print(matrix);

    for (int i = 0; i < size; i++)
        putchar(matrix.vectors[i].data[size]);
    return 0;
}
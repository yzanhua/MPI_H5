#include<stdio.h>

int add(int a, int b){
    return a + b;
}

int sum(int a[], size_t len){
    int res = 0;
    for (size_t i = 0; i < len; ++i){
        res += a[i];
    }
    return res;
}
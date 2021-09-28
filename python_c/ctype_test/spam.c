#include<stdio.h>

long add(long a, long b){
    return a + b;
}

long sum(long a[], size_t len){
    long res = 0;
    for (size_t i = 0; i < len; ++i){
        res += a[i];
    }
    return res;
}
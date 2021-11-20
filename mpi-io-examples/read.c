#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE* fp;
    
    int*  buff = malloc(sizeof(int) * 30);

    fp = fopen("./testFile", "r");
    fread(buff, sizeof(int), 30, fp);
    fclose(fp);

    for (int j = 0; j < 3; j++) {
        for (int i = 0; i < 10; i++) {
            printf("%d ", buff[j*10+i]);
        }
        printf("\n");
    }

    free(buff);
    return 0;
}
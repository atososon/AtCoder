#include <stdio.h>

int main(void){
    int k[] = {1,1,1,2,1,2,1,5,2,2,1,5,1,2,1,14,1,5,1,5,2,2,1,15,2,2,5,4,1,4,1,51};
    int j;
    scanf("%d",&j);
    printf("%d",k[j-1]);

    return 0;
}
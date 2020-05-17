#include <stdio.h>

int main(void){
    int n;
    scanf("%d",&n);
    n=n%10;
    if(n==2 || n==4 || n==5 || n==7 || n==9){
        printf("hon\n");
    }else if(n==3){
        printf("bon\n");
    }else{
        printf("pon\n");
    }
    return 0;
}
#include <stdio.h>

int main(void){
    int s,w;
    scanf("%d %d",&s,&w);
    if(s<=w){
        printf("unsafe\n");
    }else{
        printf("safe\n");
    }
    return 0;
}
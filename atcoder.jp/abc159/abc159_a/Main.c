#include <stdio.h>

int main(void){
    int n,m;
    scanf("%d %d",&n,&m);
    printf("%d",(m*(m-1)+n*(n-1))/2);
    return 0;
}
#include <stdio.h>
#include <math.h>

int main(void){
    long int a,b,c;
    scanf("%ld %ld %ld",&a,&b,&c);
    long int d=c-a-b;
    if(4*a*b<d*d && d>0){
        printf("Yes");
    }
    else{
        printf("No");
    }

    return 0;
}
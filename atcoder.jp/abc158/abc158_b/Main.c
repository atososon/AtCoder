#include <stdio.h>

int main(void){
    long int n;
    long int a;
    long int b;
    scanf("%ld %ld %ld",&n,&a,&b);
    if(n%(a+b)<=a){
        printf("%ld",n/(a+b)*a+n%(a+b));
    }
    else{
        printf("%ld",n/(a+b)*a+a);
    }
    return 0;
}
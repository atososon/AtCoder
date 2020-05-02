#include <stdio.h>

int main(void){
    long long int x;
    scanf("%lld",&x);
    long long int i=100;
    long long int count=0;
    while(x>i){
        i+=i/100;
        count++;
    }
    printf("%lld\n",count);
    return 0;
}
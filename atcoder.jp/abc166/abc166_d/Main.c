#include <stdio.h>
#include <math.h>

int main(void){
    int x;
    scanf("%d",&x);
    for(int i=-1000; i<1000; i++){
        for(int j=-1000; j<1000; j++){
            if(pow(i,5)-pow(j,5)==x){
                printf("%d %d\n",i,j);
                return 0;
            }
        }
    }
    return 0;
}
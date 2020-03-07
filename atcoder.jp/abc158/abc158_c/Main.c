#include <stdio.h>
#include <math.h>

int main(void){
    int a;
    int b;
    double s=0.0;
    double t=0.0;
    int f=0;
    scanf("%d %d",&a,&b);
    for(int i=1; i<=1000; i++){
        s=(double)i*0.08;
        t=(double)i*0.1;
        if(floor(s)==a&&floor(t)==b){
            printf("%d\n",i);
            break;
        }
        if(i==1000){
            f=1;
        }
    }
    if(f==1){
        printf("-1");
    }
	return 0;
}
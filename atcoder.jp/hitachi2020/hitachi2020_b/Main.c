#include <stdio.h>
#include <math.h>

int main(void){
    int a;
    int b;
    int m;
    int xm[100000];
    int ym[100000];
    int cm[100000];
    int ai[100000];
    int bi[100000];
    int x=100000;
    int y=100000;

    scanf("%d %d %d",&a,&b,&m);
    for(int i=0; i<a; i++){
        scanf("%d",&ai[i]);
        x=fmin(x,ai[i]);
    }
    for(int i=0; i<b; i++){
        scanf("%d",&bi[i]);
        y=fmin(y,bi[i]);
    }
    int s=x+y;
    for(int i=0; i<m; i++){
        scanf("%d %d %d",&xm[i],&ym[i],&cm[i]);
        s=fmin(s,(ai[xm[i]-1]+bi[ym[i]-1]-cm[i]));
    }
    printf("%d",s);
    
}
#include <stdio.h>
#include <math.h>

int main(void){
    int n,m;
    scanf("%d %d",&n,&m);
    int h[n];
    int ma[n];
    for(int i=0; i<n; i++){
        scanf("%d",&h[i]);
        ma[i]=0;
    }
    int a[m];
    int b[m];
    for(int i=0; i<m; i++){
        scanf("%d %d",&a[i],&b[i]);
        ma[a[i]-1]=fmax(ma[a[i]-1],h[b[i]-1]);
        ma[b[i]-1]=fmax(ma[b[i]-1],h[a[i]-1]);
    }
    int ans=0;
    for(int i=0; i<n; i++){
        if(ma[i]<h[i]){
            ans++;
        }
    }
    printf("%d\n",ans);
    return 0;
}
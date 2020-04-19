#include <stdio.h>

int main(void){
    int n;
    scanf("%d",&n);
    int a[n];
    int ans[n];
    for(int i=0; i<n; i++){
        ans[i]=0;
    }
    for(int i=0; i<n-1; i++){
        scanf("%d",&a[i]);
        ans[a[i]-1]++;
    }
    for(int i=0; i<n; i++){
        printf("%d\n",ans[i]);
    }
    return 0;
}
#include <stdio.h>

int main(void){
    int n,k;
    scanf("%d%d",&n,&k);
    int d[k];
    scanf("%d",&d[0]);
    int a[k][100];
    int count[n];
    int ans=0;
    for(int i=0; i<n; i++){
        count[i]=0;
    }
    for(int i=0; i<k; i++){
        for(int j=0; j<d[i]; j++){
            scanf("%d",&a[i][j]);
            count[a[i][j]-1]++;
        }
        if(i==k-1){
            break;
        }
        scanf("%d",&d[i+1]);
    }
    for(int i=0; i<n; i++){
        if(count[i]==0){
            ans++;
        }
    }
    printf("%d\n",ans);
    return 0;
}
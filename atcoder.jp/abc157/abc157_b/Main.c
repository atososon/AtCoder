#include <stdio.h>

int main(void){
    int a[3][3];
    int f[3][3];
    int n;
    for(int i=0; i<3; i++){
        for(int j=0; j<3; j++){
            scanf("%d",&a[i][j]);
            f[i][j]=0;
        }
    }
    scanf("%d",&n);
    int b[n];
    for(int i=0; i<n; i++){
        scanf("%d",&b[i]);
        for(int j=0; j<3; j++){
            for(int k=0; k<3; k++){
                if(b[i]==a[j][k]){
                    f[j][k]=1;
                }
            }
        }
    }
    if(f[0][0]==1&&f[0][1]==1&&f[0][2]==1 ||
    f[0][0]==1&&f[1][0]==1&&f[2][0]==1 ||
    f[0][0]==1&&f[1][1]==1&&f[2][2]==1 ||
    f[0][1]==1&&f[1][1]==1&&f[2][1]==1 ||
    f[0][2]==1&&f[1][2]==1&&f[2][2]==1 ||
    f[1][0]==1&&f[1][1]==1&&f[1][2]==1 ||
    f[2][0]==1&&f[2][1]==1&&f[2][2]==1 ||
    f[2][0]==1&&f[1][1]==1&&f[0][2]==1){
        printf("Yes\n");
    } 
    else{
        printf("No\n");
    }
}
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void){
	int n,x,y;
	int f;
	int min;
	scanf("%d %d %d",&n,&x,&y);
	int ans[n];
	for(int i=0; i<n; i++){
		ans[i]=0;
	}
	for(int i=1; i<n; i++){
		for(int j=i+1; j<=n; j++){
			min = fmin(abs(i-x)+abs(y-j)+1,j-i);
			ans[min]++;
		}
	}
	for(int i=1; i<n; i++){	
		printf("%d\n",ans[i]);
	}
	return 0;	
}

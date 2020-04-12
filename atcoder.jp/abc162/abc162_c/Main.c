#include <stdio.h>
#include <math.h>

int main(void){
	int k;
	long long int ans=0;
	int min=200;
	scanf("%d",&k);

	for(int i=1; i<=k; i++){
		for(int j=1; j<=k; j++){
			for(int l=1; l<=k; l++){
				min=fmin(i,j);
				min=fmin(min,l);
				for(int m=min; m>0; m--){
					if(i%m==0 && j%m==0 && l%m==0){
						ans+=m;
						break;
					}
				}
			}
		}
	}
	printf("%lld\n",ans);
	return 0;
}

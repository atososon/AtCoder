#include <stdio.h>

int main(void){
	int n;
	long long int ans=0;
	scanf("%d",&n);
	for(int i=1; i<=n; i++){
		if(i%3!=0 && i%5!=0){
			ans+=i;
		}
	}
	printf("%lld\n",ans);
	return 0;
}
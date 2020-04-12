#include <stdio.h>

int main(void){
	int n;
	long long int ans=0;
	scanf("%d",&n);
	char s[n+10];
	scanf("%s",s);
	long long int countr=0;
	long long int countg=0;
	long long int countb=0;
	for(int i=0; i<n; i++){
		if(s[i]=='R'){
			countr++;
		}
		if(s[i]=='G'){
			countg++;
		}
		if(s[i]=='B'){
			countb++;
		}
	}
	ans=countr*countg*countb;
	long long int i=0;
	long long int j=1;
	long long int k=2;
	while(i<=n-3){
		if(s[i]!=s[j]&&s[i]!=s[k]&&s[j]!=s[k]){
			ans--;
		}
		j++;
		k+=2;
		if(k>n-1){
			i++;
			j=i+1;
			k=i+2;
		}
	}

	printf("%lld\n",ans);
	return 0;
}
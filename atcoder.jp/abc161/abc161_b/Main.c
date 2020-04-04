#include <stdio.h>

int main(void){
	int n,m;
	scanf("%d %d",&n,&m);
	int a[n];
	int sum=0;
	int c=0;
	for(int i=0; i<n; i++){
		scanf("%d",&a[i]);
		sum+=a[i];
	}
	double line=sum/(4.0*m);
	for(int i=0; i<n; i++){
		if(a[i]>=line){
			c++;
		}
	}
	if(c>=m){
		printf("Yes\n");
	}
	else{
		printf("No\n");
	}

	return 0;
}
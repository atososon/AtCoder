#include <stdio.h>
#include <math.h>

double d(int x1, int y1, int x2, int y2){
	return sqrt(pow(x2-x1,2)+pow(y2-y1,2));
}
int main(void){
	int n;
	scanf("%d",&n);
	int x[n],y[n];
	long double sum=0.0;
	for(int i=0; i<n; i++){
		scanf("%d %d",&x[i],&y[i]);
	}
	for(int i=0; i<n; i++){
		for(int j=i+1; j<n; j++){
			sum+=d(x[i],y[i],x[j],y[j]);
		}
	}
	printf("%Lf\n",sum*2/n);
	return 0;
}
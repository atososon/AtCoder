#include <stdio.h>
#include <stdlib.h>

void sort(int* n, int len){
	int tmp;
	for(int i=0; i<len; i++){
		for(int j=len-1; j>i; j--){
			if(n[j] > n[j-1]){
				tmp=n[j];
				n[j]=n[j-1];
				n[j-1]=tmp;
			}
		}
	}
}
int desc(const void *a, const void *b){
	return *(int *)b - *(int *)a;
}

int main(void){
	int x,y,a,b,c;
	scanf("%d %d %d %d %d",&x,&y,&a,&b,&c);
	int p[a];
	int q[b];
	int r[c];
	int ans[x+y+c];
	long long int d=0;
	for(int i=0; i<a; i++){
		scanf("%d",&p[i]);
	}
	for(int i=0; i<b; i++){
		scanf("%d",&q[i]);
	}
	for(int i=0; i<c; i++){
		scanf("%d",&r[i]);
	}
	qsort(p,sizeof(p)/sizeof(*p),sizeof(*p),desc);
	qsort(q,sizeof(q)/sizeof(*q),sizeof(*q),desc);
	for(int i=0; i<x; i++){
		ans[i]=p[i];
	}
	for(int i=0; i<y; i++){
		ans[i+x]=q[i];
	}
	for(int i=0; i<c; i++){
		ans[i+x+y]=r[i];
	}
	qsort(ans,sizeof(ans)/sizeof(*ans),sizeof(*ans),desc);
	for(int i=0; i<x+y; i++){
		d+=ans[i];
	}
	printf("%lld\n",d);

	return 0;

}


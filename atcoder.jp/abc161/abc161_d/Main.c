#include <stdio.h>
#include <stdlib.h>

int main(void){
	int k;
	long long int lun[1000000];
	scanf("%d",&k);
	long long int s=11;
	int t;
	for(int i=1; i<=9; i++){
		lun[i-1]=i;
	}
	int i=8;
	int j=0;
	while(j<=k){
		long long int x=lun[j++];
		if(x%10==0){
			lun[++i]=10*x;
			lun[++i]=x*10+1;
		}else if(x%10==9){
			lun[++i]=10*x+8;
			lun[++i]=10*x+9;
		}else{
			lun[++i]=x*10+x%10-1;
			lun[++i]=10*x+x%10;
			lun[++i]=x*10+x%10+1;
		}
		/*t=s;
		while(t>0){
			if(t/10==0) break;
			if(abs(t%10-t/10%10)>1) break;
			if(t/10<10){
				lun[i]=s;
				i++;
				break;
			}
			t/=10;
		}
		s++;*/
	}
	/*for(int i=0; i<k-1; i++){
		printf("%lld\n",lun[i]);
	}*/
	printf("%lld\n",lun[k-1]);
	return 0;
}

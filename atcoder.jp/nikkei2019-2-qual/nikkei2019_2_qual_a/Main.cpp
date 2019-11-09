#include <stdio.h>

int main(void){
	int ret;
	int n;
	ret = scanf("%d",&n);
	int  c = 0;
	if(n > 1000000 || n < 1){}
	else{
		if(n%2==0)
			c=n/2-1;
		else
			c=(n-1)/2;
		//if(c != 0)
			printf("%d\n",c);
	}
	return 0;
}

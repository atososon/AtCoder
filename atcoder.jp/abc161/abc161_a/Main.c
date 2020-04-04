#include <stdio.h>

int main(void){
	int x,y,z;
	scanf("%d %d %d",&x,&y,&z);
	int tmp;
	tmp=x;
	x=y;
	y=tmp;
	tmp=x;
	x=z;
	z=tmp;

	printf("%d %d %d\n",x,y,z);

	return 0;
}
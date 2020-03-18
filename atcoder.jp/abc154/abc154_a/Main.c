#include <stdio.h>
#include <string.h>
 
int main(void){
  char s[255];
  char t[255];
  char u[255];
  int a,b;
  scanf("%s %s",s,t);
  scanf("%d %d",&a,&b);
  scanf("%s",u);
  if(strcmp(s,u)==0){
    printf("%d %d",a-1,b);
  }else if(strcmp(t,u)==0){
    printf("%d %d",a,b-1);
  }else{
    printf("%d %d",a,b);
  }
}
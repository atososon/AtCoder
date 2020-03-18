#include <stdio.h>
#include <string.h>

int main(void){
  char s[255];
  scanf("%s",s);
  for(int i=0; i<strlen(s); i++){
    printf("x");
  }
}
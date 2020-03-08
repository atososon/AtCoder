#include <stdio.h>
#include <string.h>

int main(void){
    char s[256];

    scanf("%s",s);

    if(strcmp(s,"hi")==0||strcmp(s,"hihi")==0||strcmp(s,"hihihi")==0||strcmp(s,"hihihihi")==0||strcmp(s,"hihihihihi")==0){
        printf("Yes");
    }
    else{
        printf("No");
    }
    return 0;
}
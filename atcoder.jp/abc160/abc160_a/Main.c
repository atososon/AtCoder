#include <stdio.h>
#include <string.h>

int main(void){
        char s[255];
        scanf("%s",s);
        if(s[2]==s[3]&&s[4]==s[5]){
                printf("Yes\n");
        }
        else{
                printf("No\n");
        }
}
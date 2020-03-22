#include <stdio.h>
#include <string.h>

int main(void){
    char s[255];
    int f1=0;
    int f2=0;
    scanf("%s",s);
    for(int i=0; i<(strlen(s)-1)/2; i++){
        //if(strcmp(s[i],s[(strlen(s)-1)/2-1-i])==0){
        //printf("%s\t%s\n",s[i],s[(strlen(s)-1)/2-1-i]);
        if(s[i]==s[(strlen(s)-1)/2-1-i]){
            f1++;
        }
    }
    for(int i=(strlen(s)+3)/2-1; i<strlen(s); i++){
        //if(strcmp(s[i],s[strlen(s)-1-i])==0){
        //printf("%s\t%s\n",s[i],s[strlen(s)-1-i]);
        if(s[i]==s[strlen(s)-1-i]){
            f2++;
        }
    }
    //printf("%d\t%d\n",(strlen(s)-1)/2,strlen(s)-((strlen(s)+3)/2-1));
    //printf("%d\t%d\n",f1,f2);
    if(f1==(strlen(s)-1)/2 && f2==strlen(s)-((strlen(s)+3)/2-1)){
        printf("Yes");
    }
    else{
        printf("No");
    }
}
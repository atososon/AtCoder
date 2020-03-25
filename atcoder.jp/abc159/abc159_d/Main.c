#include <stdio.h>

long long int choose(long long int n){
    return n*(n-1)/2;
}

int main(void){
    long long int n;
    scanf("%lld",&n);
    long long int a[n];
    long long int s[n];
    long long int t=0;
    long long int ans=0;;
    for(int i=0; i<n; i++){
        scanf("%lld",&a[i]);
        a[i]--;
        s[i]=0;
    }
    for(int i=0; i<n; i++){
        s[a[i]]++;        
    }
    for(int i=0; i<n; i++){
        t+=choose(s[i]);
    }
    for(int i=0; i<n; i++){
        ans=t;
        ans-=choose(s[a[i]]);
        ans+=choose(s[a[i]]-1);
        printf("%lld\n",ans);
    }
    return 0;   
}
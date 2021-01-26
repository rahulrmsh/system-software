// Symbol Table - C Language

#include<stdlib.h>
#include<string.h>
#include<stdio.h>
struct Symbol{
    int adr;
    char label[20];
}s[11];
int max = 11, count = 0;
int a[11];
int main(){
    int adr, res, i;
    char label[20];
    for(i=0;i<max;i++){
        a[i] = 0;
        s[i].adr = 0;
        strcpy(s[i].label, "");
    }
    while(1){
        
    }
}
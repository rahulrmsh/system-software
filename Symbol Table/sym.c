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
int find(int adr){
    return(adr % max);
}
int main(){
    int adr, res, i;
    char label[20];
    for(i=0;i<max;i++){
        a[i] = 0;
        s[i].adr = 0;
        strcpy(s[i].label, "");
    }
    while(1){
        printf("\n1.CREATE \n2.MODIFY \n3.SEARCH \n4.DISPLAY \n5.EXIT");
        printf("\nEnter response : ");
        scanf("%d", &res);
        if (res == 1){}
        else if (res == 2) {}
        else if (res == 3) {}
        else if (res == 4) {}
        else if (res == 5) {}
        else{
            printf("\nWrong response. Try again");
        }

    }
}
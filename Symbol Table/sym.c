// Symbol Table - C Language

#include<stdlib.h>
#include<string.h>
#include<stdio.h>
struct Symbol{
    int adr;
    char label[20];
}s[11];
int max = 11, count = 0, flag = 0, i;
int a[11];

int find(int adr){
    return(adr % max);
}

void create(int adr,char label[20],int key){
    count = 0;
    flag = 0;
    if(count < max){
        for(i=key;i<max;i++){
            if(a[i] == 0){
                flag = 1;
                a[i] = 1;
                s[i].adr = adr;
                strcpy(s[i].label, label);
                count++;
                break;
            }
        }
        if(flag == 0){
            for(i=0;i<key;i++){
                if(a[i] == 0){
                    flag = 1;
                    a[i] = 1;
                    s[i].adr = adr;
                    strcpy(s[i].label, label);
                    count++;
                    break;
                }
            }
        }
        if(flag == 1){
            printf("\nValue Entered.");
        }
    }
    else{
        printf("\nBucket Full.");
    }
}

void display(){
    printf("\nLocation\tAddress\tLabel\n");
        for(i=0;i<max;i++){

        }
       
}
int main(){
    int adr, res, key;
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
        if (res == 1){
            printf("Enter address : ");
            scanf("%d", &adr);
            printf("Enter label : ");
            scanf("%s", &label[20]);
            key = find(adr);
            create(adr, label, key);
        }
        else if (res == 2) {
            
        }
        else if (res == 3) {}
        else if (res == 4) {}
        else if (res == 5) {
            exit(0);
        }
        else{
            printf("\nWrong response. Try again");
        }

    }
}
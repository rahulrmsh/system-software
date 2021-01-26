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

void modify(int adr, char label[20]){
    flag = 0;
    for(i=0;i<max;i++){
        if(s[i].adr == adr){
            flag = 1;
            printf("Found at location : %d\n", i+1);
            strcpy(s[i].label, label);
            printf("New value changed as : %s\n", label);
            break;
        }
    }
    if(flag == 0){
        printf("Address not found. Try again.");
    }
}

void search(int adr){
    flag = 0;
    for(i=0;i<max;i++){
        if(s[i].adr == adr){
            flag = 1;
            printf("\nLocation \tAddress \tLabel\n");
            printf("%d\t\t%d\t\t%s\n",i+1,s[i].adr,s[i].label);
            break;
        }
    }
    if(flag == 0){
        printf("Address not found. Try again.");
    }
}
void display(){
    printf("\nLocation \tAddress \tLabel\n");
        for(i=0;i<max;i++){
            printf("%d\t\t%d\t\t%s\n",i+1,s[i].adr,s[i].label);
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
            scanf("%s", label);
            key = find(adr);
            create(adr, label, key);
        }
        else if (res == 2) {
            printf("Enter address : ");
            scanf("%d", &adr);
            printf("Enter label : ");
            scanf("%s", label);
            modify(adr, label);
        }
        else if (res == 3) {
            printf("Enter address : ");
            scanf("%d", &adr);
            search(adr);
        }
        else if (res == 4) {
            display();
        }
        else if (res == 5) {
            exit(0);
        }
        else{
            printf("\nWrong response. Try again");
        }

    }
}
// Dining Philosopher

#include<stdlib.h>
#include<stdio.h>
#include<ctype.h>
#include <string.h>

enum {
    THINKING,
    HUNGRY,
    EATING
} state[5];

int i, j, k, flag[5], n;
void initialize(){
    for(i = 0; i < 5; i++){
        state[i] = THINKING;
        flag[i] = 0;
    }
}
int main(){
    initialize();
    printf("| Choose from below : \n|1. Start Eating\n|2. Stop Eating\n|3. Exit\n| Enter Response : ");
    scanf("%d", &n);
    if(n == 3){
        
    }
    return 0;
}
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

int i, flag[5], n, key;
void initialize(){
    for(i = 0; i < 5; i++){
        state[i] = THINKING;
        flag[i] = 0;
    }
}
void eat(int x){
    state[x] = HUNGRY;
    if(state[x + 4 % 5] == THINKING && state[x - 1 % 5] == THINKING && state[x] == HUNGRY){
        state[x] = EATING;
        flag[x] = 1;
        printf("| %d is now eating.",x );
    }else{
        printf("| %d should wait",x );
    }
}
int main(){
    initialize();
    printf("| Choose from below : \n|1. Start Eating\n|2. Stop Eating\n|3. Exit\n| Enter Response : ");
    scanf("%d", &n);
    printf("| Enter philosopher id : ");
    scanf("%d", &key);
    if(n == 3){
        exit(0);
    }
    else if(n == 1){
        eat(key);
    }
    return 0;
}
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

int i, n, key;
void initialize(){
    for(i = 0; i < 5; i++){
        state[i] = THINKING;
    }
}
void eat(int x){
    state[x] = HUNGRY;
    if(state[(x + 4) % 5] == THINKING && state[(x - 1) % 5] == THINKING && state[x] == HUNGRY){
        state[x] = EATING;
        printf("| %d is now eating.\n",x );
    }else{
        printf("| %d should wait\n",x );
    }
}
void think(int x){
    state[x] = THINKING;
    eat((x-1)%5);
    eat((x+4)%5);
    printf("| %d stopped eating.",x );
}
int main(){
    initialize();
    printf("%d",state[0]);
    while(1){
        printf("| Choose from below : \n|1. Start Eating\n|2. Stop Eating\n|3. Exit\n| Enter Response : ");
        scanf("%d", &n);
        if(n == 3){
            exit(0);
        }else if (n > 3){
            printf("|\n| WRONG INPUT\n|\n");
        }
        printf("| Enter philosopher id : ");
        scanf("%d", &key);
        if(n == 1){
            printf("| %d", key );
            eat(key);
        }else if(n == 2){
            think(key);
        }
    }
    return 0;
}
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
    for(i = 0; i < n; i++){
        state[i] = THINKING;
        flag[i] = 0;
    }
}
int main(){
    n = 5;
    initialize();
    return 0;
}
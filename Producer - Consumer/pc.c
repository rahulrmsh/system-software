// Producer-Consumer - C Language
#include<stdlib.h>
#include<stdio.h>
#include<ctype.h>
int x = 0, y = 1, s = 1, empty = 4, full = 0, op;
int wait(int a){
    while(a <= 0){
        ;
    }
    return (--a);
}
int signal(int a){
    return (++a);
}
void produce(){
    empty = wait(empty);
    s = wait(s);
    x = (x + 1) % 5;
    printf("Producer produced item : %d", x);
    s = signal(s);
    empty = signal(s);
}
void consume(int a){
    
}
int main(){
}
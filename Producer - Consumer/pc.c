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
    full = signal(full);
}
void consume(){
    full = wait(full);
    s = wait(s);
    printf("Consumer consumed item : %d", y);
    y = (y - 1) % 5;
    s = signal(s);
    empty = signal(empty);
}
int main(){
    while (1)
    {
        printf("\n1.Produce \n2.Consume \n3.Exit");
        printf("\nenter choice");
        scanf("%d", &op);
        if (op == 1)
        {
            if ((s == 1) && (empty != 0))
                produce();
            else
            {
                printf("\nBuffer is full");
            }
        }
        else if (op == 2)
        {
            if ((s == 1) && (full != 0))
                consume();
            else
            {
                printf("\nBuffer is empty");
            }
        }
        else if (op == 3)
            exit(0);
    }
}
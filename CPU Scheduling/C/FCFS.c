// First Come First Serve - C Language

#include <stdio.h>
#include <stdlib.h>
int main() {
  int n, i, j;
  printf("Enter the number of processes  : ");
  scanf("%d", &n);
  int burst[n], average = 0, turn[n], waiting[n];
  for (i = 0; i < n; i++) {
    printf("Enter the burst time of processes : "); 
    scanf("%d", &j);
    turn[i] = 0;
    burst[i] = j;
  }

  for (i = 0; i < n; i++) {
    turn[i] = 0;
    
    for (j = 0; j <= i; j++) {

      turn[i] += burst[j];
      
    }
    waiting[i] = 0;
    for(j = 0; j < i; j++) {
        waiting[i] += burst[j];
    }
  }
  printf("Process\tBurst\tWaiting\tTurn\n");
  for (i = 0; i < n; i++) {
      printf("%d\t%d\t%d\t%d\n",i+1,burst[i], waiting[i], turn[i]);
  }
  float wait = 0.0, tSum = 0.0;
  for (i = 0; i < n; i++) {
      wait += waiting[i];
      tSum += turn[i];
  }
  printf("Average waiting time : %f\n", wait/n);
  printf("Average turn around time : %f\n", tSum/n);
}
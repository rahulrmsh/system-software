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
    waiting[n] = 0;
    for (j = 0; j < i; j++) {

      turn[i] += burst[j];
    }
    printf("%d\n",turn[i]);
    // average = average + burst[i];
  }
  for (i = 0; i < n; i++) {
      printf("%d\n",turn[i]);
  }
//   printf("Average %d", average / n);
//   printf("Average %d", average / n);
}
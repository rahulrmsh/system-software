// First Come First Serve - C Language

#include <stdio.h>
#include <stdlib.h>
int main() {
  int n, i, j;
  scanf("Enter the number of processes  : %d", &n);
  int burst[n], average, turn[n];
  for (i = 0; i < n; i++) {
    scanf("Enter the burst time of processes : %d", &j);
    burst[i] = j;
  }
  for (i = 0; i < n; i++) {
    for (j = 0; j <= i; j++) {

      turn[i] = turn[i] + burst[j];
    }
    average = average + burst[i];
  }
  printf("Average %d", average / n);
  printf("Average %d", average / n);
}
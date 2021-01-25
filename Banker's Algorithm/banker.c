//  Banker's Algorithm - C Language

#include <stdio.h>

int main(){
    int n, m, i, j, k;
    printf("Enter number of processes : ");
    scanf("%d",&n);
    printf("Enter number of resources : ");
    scanf("%d",&m);
    int alloc[n][m], max[n][m];
    for (i = 0; i < n; i++){
        printf("Enter allocated resource for process %d : \n", i+1);
        for (j = 0; j < m; j++){
            printf("Enter %d resources : ",j+1);
            scanf("%d",&alloc[i][j]);
        }
        printf("\n");
    }
    
    printf("\n");
    for (i = 0; i < n; i++){
        printf("Enter maximum resource for process %d : \n", i+1);
        for (j = 0; j < m; j++){
            printf("Enter %d resources : ",j+1);
            scanf("%d",&max[i][j]);
        }
        printf("\n");
    }
    printf("Allocated\t\t|Maximum\t\t\t\n");
    for (i = 0; i < n; i++){
        for (j = 0; j < m; j++){
            printf("%d\t",alloc[i][j]);
        }
        printf("|");
        for (j = 0; j < m; j++){
            printf("%d\t",max[i][j]);
        }
        printf("\n");
    }
    printf("\n");
    return (0);
}
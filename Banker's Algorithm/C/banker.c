//  Banker's Algorithm - C Language

#include <stdio.h>

int main(){
    int n, m, i, j, k, index = 0;
    printf("Enter number of processes : ");
    scanf("%d",&n);
    printf("Enter number of resources : ");
    scanf("%d",&m);
    int alloc[n][m], max[n][m], need[n][m], avail[m], flag[n], ans[n];
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
    printf("\n");
    printf("Enter available resources \n");
    for (j = 0; j < m; j++){
        printf("Enter %d resources : ",j+1);
        scanf("%d",&avail[j]);
    }
    printf("\n");
    for (i = 0; i < n; i++){
        flag[i] = 0;
        for (j = 0;j<m;j++){
            need[i][j] = max[i][j] - alloc[i][j];
        }
    }
    printf("\tAllocated\t|\tMaximum \t|\tNeed\n");
    for (i = 0; i < n; i++){
        for (j = 0; j < m; j++){
            printf("%d\t",alloc[i][j]);
        }
        printf("|");
        for (j = 0; j < m; j++){
            printf("%d\t",max[i][j]);
        }
        printf("|");
        for (j = 0; j < m; j++){
            printf("%d\t",need[i][j]);
        }
        printf("\n");
    }
    i = 0;
    while(1){
        if(flag[i] == 0){
            int log = 0;
            for (j = 0; j < m; j++){
                if(need[i][j] > avail[j]){
                    log = 1;
                    break;
                }
            }
            if(log == 0){
                flag[i] = 1;
                for (k = 0; k < m; k++){
                    avail[k] = alloc[i][k] + avail[k];
                }
                ans[index++] = i;
            };
        }
        if(i < n){i++;}
        else{i = 0;}   
        if(index == n -1){
            break;
        }        

    }
    printf("\nFollowing is the SAFE Sequence\n"); 
    for(i = 0; i< n-1;i++){
        printf("P%d->\t",ans[i]);
    }
    printf("P%d\n", ans[n+1]);
    return (0);
}
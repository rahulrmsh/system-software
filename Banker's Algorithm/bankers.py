# Banker's Algorithm - Python

n = int(input("Enter number of processes: "))
m = int(input("Enter number of resources: "))
print("Enter resource per processes: \n")
alloc = []
maximum = []
avail = []
need = []
ans = []
flag = []
for i in range(n):
    alloc.append(list(map(int, input("Enter allocated resource for process {} : ".format(i+1)).split())))
    flag.append(0)
for i in range(n):
    maximum.append(list(map(int, input("Enter maximum resource for process {} : ".format(i+1)).split())))
avail.append(list(map(int, input("Enter available resource : ").split())))
for i in range(n):
    for j in range(m):
        need[i].append(maximum[i][j] - alloc[i][j])
i = 0
while(1):
    if(flag[i] == 0):
        log = 0
        for j in range(m):
            if need[i][j] > avail[j]:
                log = 1
                break
        if log == 0:
            ans.append(i)
            for j in range(m):
                avail[j] = avail[j] + alloc[i][j]
            
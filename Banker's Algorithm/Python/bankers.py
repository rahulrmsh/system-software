# Banker's Algorithm - Python

n = int(input("Enter number of processes: "))
m = int(input("Enter number of resources: "))
print("\nEnter resource per processes \n")
alloc = []
maximum = []
avail = []
need = []
for i in range(n):
    need.append([])
ans = []
flag = []
for i in range(n):
    alloc.append(list(map(int, input("Enter allocated resource for process {} : ".format(i+1)).split(','))))
    flag.append(0)
for i in range(n):
    maximum.append(list(map(int, input("Enter maximum resource for process {} : ".format(i+1)).split(','))))
counter =  input("Enter available resource : ").split(',')
for i in counter:
    avail.append(int(i))
for i in range(n):
    for j in range(m):
        need[i].append(maximum[i][j] - alloc[i][j])
i = 0
while(1 and len(ans) < n):
    try:
        if(flag[i] == 0):
            log = 0
            for j in range(m):
                if need[i][j] > avail[j]:
                    log = 1
                    break
            if log == 0:
                flag[i] = 1
                for j in range(m):
                    avail[j] = alloc[i][j] + avail[j]
                ans.append(i)
        if i < n - 1:
            i += 1
        else:
            i = 0
        if len(ans) == n:
            break
    except :
        print(i)
        break
print("\nFollowing is the SAFE Sequence\n");
for i in range(len(ans)-1):
    print("P{}->\t".format(ans[i]), end =" ")
print("P{}".format(ans[i+1]))
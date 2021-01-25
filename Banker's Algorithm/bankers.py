# Banker's Algorithm - Python

n = int(input("Enter number of processes: "))
m = int(input("Enter number of resources: "))
print("Enter resource per processes: \n")
alloc = []
maximum = []
avail = []
for i in range(n):
    alloc.append(list(map(int, input("Enter allocated resource for process {} : ".format(i+1)).split())))
for i in range(n):
    maximum.append(list(map(int, input("Enter maximum resource for process {} : ".format(i+1)).split())))
avail.append(list(map(int, input("Enter available resource : ").split())))

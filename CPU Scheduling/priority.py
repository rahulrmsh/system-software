from prettytable import PrettyTable

n = int(input("\n| Enter Number of Processes : "))
processList = [(i+1) for i in range(n)]
burstList = []
priorityList = []
for i in range(n):
    burstList.append(int(input("| Enter the Burst Time of Process {} : ".format(i+1))))
    priorityList.append(int(input("| Enter the Priority of Process {} : ".format(i+1))))
shortList = [["0"]]
shortList = [[pid, key, burst] for pid, key, burst in zip(processList, priorityList, burstList) if [pid, key, burst] not in shortList]
shortList = (sorted(shortList, key= lambda x:x[1]))
shortList[0].append(0)
shortList[0].append(shortList[0][2])
for i in range(1, n):
    shortList[i].append(shortList[i-1][3]+shortList[i-1][2])
    shortList[i].append(shortList[i-1][4]+shortList[i][2])
t = PrettyTable(['Process Id','Priority', 'Burst Time', 'Waiting Time', 'Turn Around Time'])
for i in range(n):
    t.add_row([shortList[i][0], shortList[i][1], shortList[i][2], shortList[i][3], shortList[i][4]])
print(t)
print("| Average Waiting Time : {}".format(round(sum(x[3] for x in shortList[0:])/n, 2)))
print("| Average Turn Around Time : {}\n".format(round(sum(x[4] for x in shortList[0:])/n,2)))
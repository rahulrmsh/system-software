from prettytable import PrettyTable
n = int(input("\n| Enter Number of Processes : "))
processList = [(i+1) for i in range(n)]
burstList = []
for i in range(n):
    burstList.append(int(input("| Enter the Burst Time of Process {} :".format(i+1))))
waitingList = [0]
turnAroundTimeList = [burstList[0]]
for i in range(1, n):
    waitingList.append(waitingList[i-1]+burstList[i-1])
    turnAroundTimeList.append(turnAroundTimeList[i-1]+burstList[i])
t = PrettyTable(['Process Id', 'Burst Time', 'Waiting Time', 'Turn Around Time'])
for i, burst, wait, turn in zip(processList, burstList, waitingList, turnAroundTimeList):
    t.add_row([i, burst, wait, turn])
print(t)
print("| Average Waiting Time : {}".format(round(sum(waitingList)/n,2)))
print("| Average Turn Around Time : {}\n".format(round(sum(turnAroundTimeList)/n,2)))
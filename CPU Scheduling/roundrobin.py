from prettytable import PrettyTable

processList = []
n = 0
quantum = 0
burstList = []
copyBurstList = []
waitingList = []
turnAroundTimeList = []

def inputCycle():
    global n
    global quantum
    global copyBurstList
    global turnAroundTimeList
    global waitingList
    n = int(input("\n| Enter Number of Processes : "))
    quantum = int(input("| Enter Required Time Quantum : "))
    for i in range(n):
        processList.append(i+1)
        burstList.append(int(input("| Enter the Burst Time of Process {} : ".format(i+1))))
        waitingList.append(0)
        turnAroundTimeList.append(0)
        copyBurstList.append(burstList[i])

def timeManager(indexKey):
    global copyBurstList
    global turnAroundTimeList
    global waitingList
    if(copyBurstList[indexKey] > quantum):
        turnAroundTimeList[indexKey] = turnAroundTimeList[indexKey] + quantum
        copyBurstList[indexKey] = copyBurstList[indexKey] - quantum
    else:
        turnAroundTimeList[indexKey] = turnAroundTimeList[indexKey] + copyBurstList[indexKey]
        waitingList[indexKey] = turnAroundTimeList[indexKey] - copyBurstList[indexKey]
        copyBurstList[indexKey] = 0
        turnAroundTimeList[indexKey] = waitingList[indexKey]+burstList[indexKey]


def roundRobin():
    while(sum(copyBurstList) != 0):
        for i in range(n):
            if(copyBurstList[i] <= 0):
                continue
            else:
                timeManager(i)


def printResults():
    t = PrettyTable(['Process Id', 'Burst Time', 'Waiting Time', 'Turn Around Time'])
    for i in range(n):
        t.add_row([processList[i], burstList[i], waitingList[i], turnAroundTimeList[i]])
    print(t)
    print("| Average Waiting Time : {}".format(round(sum(waitingList)/n, 2)))
    print("| Average Turn Around Time : {}\n".format(round(sum(turnAroundTimeList)/n,2)))

def main():
    inputCycle()
    roundRobin()
    printResults()

if __name__=="__main__": 
    main() 
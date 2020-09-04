dirName = input("| Enter Core Directory Name : ")
print('|\n|\033[92m Core Directory Created\033[0m')
subFileName = {}
subDirName = {}
fileListKey = [dir]
finalList = '.'
responseCode = 1
while(responseCode < 3 and responseCode > 0):
    print('|\n| Operations\n|\n| 1.Create File\n| 2.View All Files\n| 3.Exit\n|')
    responseCode = int(input('| Enter Response : '))
    if(responseCode == 1):
        fileId = input("| Enter File Name : ")
        locationId = input('| Enter File Location : ')
        locationId = locationId.split('/')
        i = 0
        if(locationId[0] == dirName):
            while(i < len(locationId) - 1):
                if(locationId[i] in subDirName):
                    try:
                        subDirName[locationId[i]].index(locationId[i+1])
                    except ValueError:
                        subDirName[locationId[i]].append(locationId[i+1])
                else:
                    subDirName[locationId[i]] = [locationId[i+1]]
                i = i + 1
            if(locationId[i] in subFileName):
                try:
                    try:
                        subFileName[locationId[i]].index(fileId)
                        print('|\n|\033[93m File Name Already Exits. Try Again\033[0m')
                    except ValueError:
                        subFileName[locationId[i]].append(fileId)
                        print('|\n|\033[92m File Created\033[0m')
                except : pass
            else:
                subFileName[locationId[i]] = [fileId]
                print('|\n|\033[92m File Created\033[0m')
        else:
            print('|\n|\033[93m Wrong Core Directory Name. Try Again\033[0m')
    if(responseCode == 2):
        print("| Directories : {}\n| Files : {}".format(subDirName, subFileName))
print("|\n| Thank You. Bye")
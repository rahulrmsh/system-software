dirName = input("| Enter Core Directory Name : ")
print('|\n|\033[92m Core Directory Created\033[0m')
coreFileName = []
subFileName = {}
responseCode = 1
while(responseCode < 5 and responseCode > 0):
    print('|\n| Operations\n|\n| 1.Create File\n| 2.Delete File\n| 3.Search in Directory\n| 4.View All Files\n| 5.Exit\n|')
    responseCode = int(input('| Enter Response : '))
    if(responseCode == 1):
        fileId = input("| Enter File Name : ")
        locationId = input('| Enter File Location : ')
        locationId = locationId.split('/')
        if(locationId[0] == dirName):
            if(len(locationId) == 1):
                try:
                    coreFileName.index(fileId)
                    print('|\n|\033[93m File Name Already Exits. Try Again\033[0m')
                except ValueError:
                    coreFileName.append(fileId)
                    print('|\n|\033[92m File Created\033[0m')
            elif(len(locationId) == 2):
                if(locationId[1] in subFileName):
                    try:
                        subFileName[locationId[1]].index(fileId)
                        print('|\n|\033[93m File Name Already Exits. Try Again\033[0m')
                    except ValueError:
                        subFileName[locationId[1]].append(fileId)
                        print('|\n|\033[92m File Created\033[0m')
                else:
                    subFileName[locationId[1]] = [fileId]
                    print('|\n|\033[92m File Created\033[0m')
        else:
            print('|\n|\033[93m Wrong Directory Name. Try Again\033[0m')
    elif (responseCode == 2):
        fileId = input("|\n| Enter Name File to be Deleted : ")
        done = False
        while (1):
            try:
                for files in coreFileName:
                    if(files == fileId):
                        idValue = coreFileName.index(fileId)
                        coreFileName.pop(idValue)
                        print('|\n|\033[91m File Deleted\033[0m')
                        done = True
            except : pass
            try:
                for dirs in subFileName:
                    for files in subFileName[dirs]:
                        if(files == fileId):
                            if(len(subFileName[dirs]) == 1):
                                del subFileName[dirs]
                            else:
                                idValue = coreFileName.index(fileId)
                                coreFileName.pop(idValue)
                                print('|\n|\033[91m File Deleted\033[0m')
                            done = True
            except : pass
            if(done):
                break
            else:
                print('|\n|\033[93m File Not Found. Try Again\033[0m')
                break
    elif (responseCode == 3):
            fileId = input("|\n| Enter Name File to Search : ")
            done = False
            while (1):
                for files in coreFileName:
                    if(files == fileId):
                        print('|\n|\033[92m File Found As {}/{}\033[0m'.format(dirName,files))
                        done = True
                for dirs in subFileName:
                    for files in subFileName[dirs]:
                        if(files == fileId):
                            print('|\n|\033[92m File Found As {}/{}/{}\033[0m'.format(dirName,dirs,files))
                            done = True
                if(done):
                    break
                else:
                    print('|\n|\033[93m File Not Found. Try Again\033[0m')
                    break
    elif (responseCode == 4):
        print("|\n|\033[92m Files : \033[0m")
        for files in coreFileName:
            print('|\033[92m {}/{}\033[0m'.format(dirName, files))
        for dirs in subFileName:
            for files in subFileName[dirs]:
                print('|\033[92m {}/{}/{}\033[0m'.format(dirName, dirs, files))
print("|\n| Thank You. Bye")

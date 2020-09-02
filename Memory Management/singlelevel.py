dirName = input("| Enter Directory Name : ")
print('|\n|\033[92m Directory Created\033[0m')
fileName = []
responseCode = 1
while(responseCode < 5 and responseCode > 0):
    print('|\n| Operations\n|\n| 1.Create File\n| 2.Delete File\n| 3.Search in Directory\n| 4.View All Files\n| 5.Exit\n|')
    responseCode = int(input('| Enter Response : '))
    if(responseCode == 1):
        fileId = input("| Enter File Name : ")
        try:
            fileName.index(fileId)
            print('|\n|\033[93m File Name Already Exits. Try Again\033[0m')
        except ValueError:
            fileName.append(fileId)
            print('|\n|\033[92m File Created\033[0m')
    elif (responseCode == 2):
        fileId = input("|\n| Enter Name File to be Deleted : ")
        try:
            idValue = fileName.index(fileId)
            fileName.pop(idValue)
            print('|\n|\033[91m File Deleted\033[0m')
        except ValueError:
            print('|\n|\033[93m File Name Not Found. Try Again\033[0m')
    elif (responseCode == 3):
        fileId = input("|\n| Enter Name File to Search : ")
        try:
            idValue = fileName.index(fileId)
            print('|\n|\033[92m File Found As {}/{}\033[0m'.format(dirName,fileName[idValue]))
        except ValueError:
            print('|\n|\033[93m File Name Not Found. Try Again\033[0m')
    elif (responseCode == 4):
        print("|\n|\033[92m Files : \033[0m")
        for files in fileName:
            print('|\033[92m {}/{}\033[0m'.format(dirName, files))
print("|\n| Thank You. Bye")

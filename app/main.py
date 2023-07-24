import sys
from utils import fileUtils

baseDIR = sys.argv[1]
option,optionArgument="",""

try:
    option = sys.argv[2]
except Exception as e:
    print("Exception at option parse")
    print(e)
    pass

try:
    allFiles = fileUtils.getFiles(baseDIR=baseDIR)
    if(option == "-e"):
        excludedFiles = []

        for i in range(3,len(sys.argv)):
            excludedFiles.append(sys.argv[i])
        
        allFiles = [file for file in allFiles if not any([True for i in excludedFiles if file.find(i)!=-1])]
    
    pdfFiles,imageFiles,docFiles,otherFiles = fileUtils.getFilesSorted(allFiles)

    fileUtils.createFoldersifNotExists(baseDIR=baseDIR,files=allFiles)

    fileUtils.putFilesInFolder(baseDIR=baseDIR,pdfFiles=pdfFiles,imageFiles=imageFiles,docFiles=docFiles,otherFiles=otherFiles)

except Exception as e:
    print(e)
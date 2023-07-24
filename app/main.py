import sys
from utils import fileUtils

baseDIR = sys.argv[1]
option,optionArgument="",""
try:
    option = sys.argv[2]
    optionArgument = sys.argv[3]
except Exception as e:
    print(e)
    pass
try:
    allFiles = fileUtils.getFiles(baseDIR=baseDIR)

    pdfFiles,imageFiles,docFiles,otherFiles = fileUtils.getFilesSorted(allFiles)

    fileUtils.createFoldersifNotExists(baseDIR=baseDIR,files=allFiles)

    fileUtils.putFilesInFolder(baseDIR=baseDIR,pdfFiles=pdfFiles,imageFiles=imageFiles,docFiles=docFiles,otherFiles=otherFiles)

except Exception as e:
    print(e)
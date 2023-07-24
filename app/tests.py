from utils import fileUtils

if __name__ == "__main__":
    
    baseDIR="testdir/"
    
    allFiles = fileUtils.getFiles(baseDIR=baseDIR)

    pdfFiles,imageFiles,docFiles,otherFiles = fileUtils.getFilesSorted(allFiles)

    fileUtils.createFoldersifNotExists(baseDIR=baseDIR,files=allFiles)

    fileUtils.putFilesInFolder(baseDIR=baseDIR,pdfFiles=pdfFiles,imageFiles=imageFiles,docFiles=docFiles,otherFiles=otherFiles)

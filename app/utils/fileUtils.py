# Files added to 
import shutil
import os

def getFiles(baseDIR):
    return os.listdir(baseDIR)


def getFilesSorted(files):
    pdfFiles=[]
    imageFiles=[]
    docFiles=[]
    otherFiles = []

    for file in files:
        if file.endswith(".pdf"):
            pdfFiles.append(file)
        elif file.endswith(".jpeg") or file.endswith(".svg") or file.endswith(".jpg") or file.endswith(".png") or file.endswith(".svg") or file.endswith(".tiff"):
            imageFiles.append(file)
        elif file.endswith(".doc") or file.endswith(".docx") or file.endswith(".txt"):
            docFiles.append(file)
        else:
            otherFiles.append(file)
    return pdfFiles,imageFiles,docFiles,otherFiles

def createFoldersifNotExists(baseDIR,files):
    try:
        files.index("Pdf")
    except Exception:
        os.mkdir(f"{baseDIR}/Pdf")

    try:
        files.index("Documents")
    except Exception:
        os.mkdir(f"{baseDIR}/Documents")

    try:
        files.index("Images")
    except Exception:
        os.mkdir(f"{baseDIR}/Images")
    try:
        files.index("Other")
    except Exception:
        os.mkdir(f"{baseDIR}/Other")

def putFilesInFolder(baseDIR,pdfFiles,imageFiles,docFiles,otherFiles):

    for file in pdfFiles:
        shutil.move(f"{baseDIR}/{file}",f"{baseDIR}/Pdf/{file}")

    for file in imageFiles:
        shutil.move(f"{baseDIR}/{file}",f"{baseDIR}/Images/{file}")

    for file in docFiles:
        shutil.move(f"{baseDIR}/{file}",f"{baseDIR}/Documents/{file}")

    for file in otherFiles:
        shutil.move(f"{baseDIR}/{file}",f"{baseDIR}/Other/{file}")

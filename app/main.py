import os
import shutil
files = os.listdir("testdir/")
pdfFiles=[]
imageFiles=[]
docFiles=[]
otherFiles = []

try:
    files.index("Pdf")
except Exception:
    os.mkdir("testdir/Pdf")

try:
    files.index("Documents")
except Exception:
    os.mkdir("testdir/Documents")

try:
    files.index("Images")
except Exception:
    os.mkdir("testdir/Images")

try:
    files.index("Other")
except Exception:
    os.mkdir("testdir/Other")

for file in files:
    if file.endswith(".pdf"):
        pdfFiles.append(file)
    elif file.endswith(".jpeg") or file.endswith(".svg") or file.endswith(".jpg") or file.endswith(".png") or file.endswith(".svg") or file.endswith(".tiff"):
        imageFiles.append(file)
    elif file.endswith(".doc") or file.endswith(".docx") or file.endswith(".txt"):
        docFiles.append(file)
    else:
        otherFiles.append(file)

for file in pdfFiles:
    shutil.move(f"testdir/{file}",f"testdir/Pdf/{file}")


for file in imageFiles:
    shutil.move(f"testdir/{file}",f"testdir/Images/{file}")


for file in docFiles:
    shutil.move(f"testdir/{file}",f"testdir/Documents/{file}")


for file in otherFiles:
    shutil.move(f"testdir/{file}",f"testdir/Other/{file}")

#shutil.move("testdir/file3.pdf","testdir/Documents/file3.pdf")

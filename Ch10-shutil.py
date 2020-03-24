import shutil, send2trash, os, zipfile
from pathlib import Path

def copySingleFile():
    CWD = Path.cwd()
    shutil.copy(CWD / 'Remark', CWD / 'Remark_Backup' )

def copyDir():
    CWD = Path.cwd()
    shutil.copytree(CWD, CWD/'Backup')

def renameFile():
    # use move function to rename file name
    CWD = Path.cwd()
    shutil.move(CWD / 'Remark', CWD / 'Remark.txt')

def deleteFile():
    print("use os.unlink('Path') to delete file")
    print("use os.rmdir('Path') to delete folder")
    print("use shutil.rmtree('Path') to delete folder, subfolder and file")
    print("use send2trash module to safely delete file")

def send2trashFile():
    #ERROR
    CWD = Path.cwd()
    send2trash.send2trash(CWD / 'Remark_Backup')

def loopFolder():
    for folderName, subFolders, fileNames in os.walk(Path.cwd()):
        print("The current folder is %s" %folderName)
        for sFolder in subFolders:
            print("SubFolder is %s" %sFolder)
        
        for fName in fileNames:
            print("File inside %s" %fName)

def createZipFile():
    zipFilePath = r"C:\TEMP\AutomatePython.zip"
    currentDir = Path.cwd()
    newZipFile = zipfile.ZipFile(zipFilePath, "w")
    
    for fileName in os.listdir(currentDir):
        addFilePath = str(currentDir) + "\\" + fileName
        newZipFile.write(fileName , compress_type=zipfile.ZIP_DEFLATED)
    
    newZipFile.close()

def readZipFile():
    zipFilePath = r"C:\TEMP\AutomatePython.zip"
    newZipFile = zipfile.ZipFile(zipFilePath)
    print(list(newZipFile.namelist()))

def extractZipFile():
    zipFilePath = r"C:\TEMP\AutomatePython.zip"
    newZipFile = zipfile.ZipFile(zipFilePath)
    newZipFile.extractall(r"C:\TEMP\Auto")
    # OR Extract singel file
    # newZipFile.extrat("FileInsideZip")
    newZipFile.close()
    
createZipFile()
#extractZipFile()
#readZipFile()
#loopFolder()
#send2trashFile()
#renameFile()
#copyDir()
#copySingleFile()
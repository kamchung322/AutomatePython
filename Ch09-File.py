from pathlib import Path
import os

def RunPath():
    #print(Path('spam', 'bacon', 'eggs'))
    print(Path.cwd())
    # os.chdir("C:\\")

    print(Path.cwd())
    #print(Path.home())

def MakeDir():
    # os.makedirs('C:\ABC\DEF\HIJ') 
    # will make dir ABC, DEF, HIJ even ABC is not exist
    # but path().mkdir() will not 
    NewPath = Path(Path.cwd(),"ByPython")
    Path(NewPath).mkdir()

def PathStructure():
    p = Path(Path(Path.cwd(), "Ch09-File.py"))
    print("Path : %s" %p)
    print("Root folder : %s" %p.anchor)
    print("Drive : %s" %p.drive)
    print("Parent Folder : %s" %p.parent)
    print("File Name : %s" %p.stem)
    print("File Extension : %s" %p.suffix)
    print("Parents[3] : %s" %p.parents[3])

def GetFileFolderInfo():
    p = Path(Path(Path.cwd(), "Ch09-File.py"))
    p = Path.cwd()
    print("File size : %s" %os.path.getsize(p))
    print("Files : %s" %os.listdir(Path.cwd()))
    #print(".py file : %s" %list(p.glob(".py")))
    list(p.glob(".py"))

def ValidatePath():
    winDir = Path('C:/Windows')
    print("'%s' is exist ? : %s" %(winDir, winDir.exists() ))
    print("'%s' is folder ? : %s" %(winDir, winDir.is_dir() ))
    print("'%s' is file ? : %s" %(winDir, winDir.is_file() ))

def ReadWriteFile():
    p = Path(Path.cwd(), "CreatedByPython.txt")
    p.write_text(p.read_text() + "\n" + "Everything is fine")
    print(p.read_text())

def ReadFile():
    p = Path(Path.cwd(), "CreatedByPython.txt")
    txtFile = open(p)
    txtAllContent = txtFile.read()
    print(txtAllContent)
    #txtLine = txtFile.readlines()
    #print(txtLine)
    txtFile.close()

def WriteFile():
    p = Path(Path.cwd(), "CreatedByPython.txt")
    txtFile = open(p, 'w')
    txtFile.write("Write by file.write")
    txtFile.close()

WriteFile()
ReadFile()
#ReadWriteFile()
#RunPath()
#PathStructure()
#GetFileFolderInfo()
#ValidatePath()

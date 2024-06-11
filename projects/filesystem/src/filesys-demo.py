import os
import time


# HELPER FUNCTIONS

def ensure_dir(dirName):
    try:
        flist = os.listdir()
        if not dirName in flist:
            os.mkdir(dirName)
        return True
    except Exception as e:
        print("Error: ", e)
        return False
    

def delete_dir(dirName):
    try:
        flist = os.listdir()
        if dirName in flist:
            os.rmdir(dirName)
            return True
        else:
            return False
    except Exception as e:
        print("Error: ", e)
        return False

def get_rtc_timestamp():
    from machine import RTC
    dt=RTC().datetime()
    return "{}-{:02}-{:02} {:02}:{:02}:{:02}".format(dt[0],dt[1],dt[2],dt[4],dt[5],dt[6])

def get_timestamp():
    dt =time.localtime()
    return "{}-{:02}-{:02} {:02}:{:02}:{:02}".format(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5])



# DEMOS

def dir_demo():
    try:
        # directory info and create subdir
        print("List of files in the current directory '{0}': {1}".format(os.getcwd(), os.listdir()))

        newDir = 'newdir'
        subDir = 'newsubdir'

        print(("Directory '" + newDir + "' exists" if ensure_dir(newDir) else  "Error creating directory "+ newDir))
        print("Directory '" + newDir + "' exists") if ensure_dir(newDir) else  print("Error creating directory "+ newDir)

        print("Status of dir '" + newDir+"' :", os.stat(newDir))

        # Change the current working directory
        print("\nCreate subdir")
        os.chdir(newDir)
        print("List of files in the current directory '{0}': {1}".format(os.getcwd(), os.listdir()))
        print("Directory '" + subDir + "' exists") if ensure_dir(subDir) else  print("Error creating directory "+ subDir)
        
        # Non-empty directories cannot be deleted:
        print("\nTry to delete non-empty directory")
        os.chdir('/')
        print("Directory '" + newDir + "' deleted") if delete_dir(newDir) else print("Error deleting directory '" + newDir + "'")

        print("\nDelete subdir")
        os.chdir(newDir)
        print("Directory '" + subDir + "' deleted") if delete_dir(subDir) else print("Error deleting directory '" + subDir + "'")
        os.chdir('/')
        
        print("\nDelete recently created dir twice")
        print("Directory '" + newDir + "' deleted") if delete_dir(newDir) else print("Error deleting directory '" + newDir + "'")
        print("Directory '" + newDir + "' deleted") if delete_dir(newDir) else print("Error deleting directory '" + newDir + "'")
        
        print("\nList of files in the current directory '{0}': {1}".format(os.getcwd(), os.listdir()))

    except Exception as e:
        print("Error: ", e)

def file_demo():
    try:
        dataDir='data'
        filename='data.txt'
        ensure_dir(dataDir)
        os.chdir(dataDir)
        if not filename in os.listdir():
            print("Creating file: ", filename)
            f = open(filename, 'w')
        else:
            print("File already exists: ", filename)
            f = open(filename, 'a')
        with f:
            i = 1
            while i <= 5:
                f.write("{}\t{}%\r\n".format(get_timestamp(),i))
                i += 1
                time.sleep(1)
            f.close()
            f.close()
        with open(filename,'r',encoding='utf-8') as f:
            content=f.read()
            f.close()
            print("Content: ")
            print(content)
        print("Content of directory:",os.listdir())
        status=os.stat(filename)
        print("File info:", status)
        print("File size in bytes:", status[6])
    except Exception as e:
        print("Error: ", e)

dir_demo()
file_demo()

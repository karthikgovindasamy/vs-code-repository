import os
def disk_usage(path):
    total=os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath=os.path.join(path,filename)
            filesize=os.path.getsize(childpath)
            if filesize!=None:
                total+=filesize
    print total

disk_usage(os.getcwd())
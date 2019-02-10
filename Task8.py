import hashlib
import os

x = input("Enter the extnfile:")
def fl(fname):
    mpfile = hashlib.fl()
    with open(fname, "rb") as f:
        for cks in iter(lambda: f.read(4096), b""):
            mpfile.update(cks)
    return mfile.hexdigest()

PATH = os.getenv("HOME")
def file(extension):
    for root, subFolder, files in os.walk(PATH):
        for i in files:
            if i.endswith("."+ str(extension)):
                path = str(os.path.join(root,i))
                print(path," ",fl(path))

file(x)


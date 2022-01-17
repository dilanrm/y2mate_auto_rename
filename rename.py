import os
import sys

args = sys.argv
path = os.path.abspath(os.getcwd())

if len(args) > 1:
    path = args[1]
files = next(os.walk(path))[2]

# print(files)
# print(path)
for i, file in enumerate(files):
    try:
        nama_baru = file.replace("y2mate.com - ", "")
        os.rename(os.path.join(path, file), os.path.join(path,nama_baru))
    except OSError as e:
        print("file " + file + " is being used. ")
    if "y2mate.com - " in file: print("Process done!")
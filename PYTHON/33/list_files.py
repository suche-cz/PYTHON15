# list_files.py

import os

path1 = "c:\\Users\\suche\\Downloads"
path2 = "c:/Users/suche/Downloads"
path3 = r"c:\Users\suche\Downloads"  # raw-string

print(path1)
print(path2)
print(path3)

folder_exists = os.path.exists(path1)
is_dir = os.path.isdir(path1)
is_file = os.path.isfile(path1)

print(folder_exists)
print(is_dir)
print(is_file)

files = os.listdir(path1)
# print(files)

for item in files:
    if item.endswith(".jpg") and len(item) < 20:
        print(item)

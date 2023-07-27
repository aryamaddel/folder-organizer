import os
import shutil

folder_to_track = r'C:\Users\Arya\Downloads'
os.chdir(folder_to_track)

for filename in os.listdir(folder_to_track):
    if os.path.isdir(filename):
        continue

    file_ext = os.path.splitext(filename)[1]

    folder_name = file_ext[1:].upper()

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    shutil.move(filename, folder_name)

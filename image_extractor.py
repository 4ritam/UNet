import os
import shutil

# Specify the source directory where the files are located
source_dir = "segmented"

# Specify the destination directory where you want to move the files
dest_dir = "leaf"
os.makedirs(dest_dir, exist_ok=True)


# Loop through all subdirectories in the source directory
for dirs in os.listdir(source_dir):
    # if "healthy" in dirs:
        current_dir = source_dir + "/" + dirs
        files = os.listdir(current_dir)
        tenth = len(files)
        for file in files[:tenth]:
            print(file)
            # # Get the full path of the file
            file_path = current_dir + '/' + file
            # # Move the file to the destination directory
            shutil.copy(file_path, dest_dir)

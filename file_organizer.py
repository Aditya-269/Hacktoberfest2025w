import os
import shutil

# Path to organize
path_to_organize = input("Enter the folder path to organize: ")

# File types and their target folders
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Python": [".py"]
}

# Create folders if not exist
for folder in file_types.keys():
    folder_path = os.path.join(path_to_organize, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Organize files
for file in os.listdir(path_to_organize):
    file_path = os.path.join(path_to_organize, file)
    if os.path.isfile(file_path):
        moved = False
        for folder, extensions in file_types.items():
            if file.lower().endswith(tuple(extensions)):
                shutil.move(file_path, os.path.join(path_to_organize, folder, file))
                moved = True
                break
        if not moved:
            # Files that don't match any type
            other_folder = os.path.join(path_to_organize, "Others")
            if not os.path.exists(other_folder):
                os.makedirs(other_folder)
            shutil.move(file_path, os.path.join(other_folder, file))

print("✅ Files have been organized successfully!")

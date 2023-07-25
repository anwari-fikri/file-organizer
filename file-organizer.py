import os
import shutil

path = "C:\\Users\\AK MD ANWARI FIKRI\\Downloads\\"
filename = os.listdir(path)

folders = {
    "images": [".jpg", ".jpeg", ".png", ".gif"],
    "exe": [".exe", ".msi"],
    "videos": [".mp4", ".avi", ".mov"],
    "office": [".docx", ".xlsx", ".pptx", ".pdf"],
    "zip": [".zip", ".rar", ".7z", ".tar", ".gz", ".tar.gz", ".tgz"]
}


for folder in folders:
    if not os.path.exists(os.path.join(path, folder)):
        os.makedirs(os.path.join(path, folder))

for file in filename:
    for folder, extensions in folders.items():
        for ext in extensions:
            if ext in file and not os.path.exists(os.path.join(path, folder, file)):
                shutil.move(os.path.join(path, file), os.path.join(path, folder, file))
                break

import os
for foldername, subfolders, filenames in os.walk(r"C:\Users\Admin\Desktop"):
    print(f"Contents of {foldername}\nsubfolders:\n")
    for subfolder in subfolders:
        print(f"\t{subfolder}\n")
    print("files:")
    for files in filenames:
        print(f"\t{files}\n")
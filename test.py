#Bare bones work
import os
def files_list():
    "Lists all files present in the directory"
    files = [f for f in os.listdir() if os.path.isfile(f) and f.endswith((".csv"))]
    return files
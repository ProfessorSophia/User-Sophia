import os
import subprocess

# ------------------------
# Getting files
# ------------------------

# Path to the directory
path = '/User-Sophia/User-Sophia/text'

# List all files in the directory
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

# ------------------------
# Run the files that end in
# .ahk
# ------------------------


for file in files:
    if file.endswith('.ahk'):
        subprocess.run([
            r"C:\Program Files\AutoHotkey\v2\AutoHotkey64.exe",  # Use raw string for backslashes
            Path + "\\" + file
        ])
#        


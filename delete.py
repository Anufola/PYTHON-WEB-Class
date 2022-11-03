import os
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
    print("File deleted succesfully")
else:
    print("File doesn't exist")

# read from the file and determine the highest number
# Writing Files

import os

with open("/home/robuntu/Sairam/ICS4U-Classwork/learning_python/Tell me what u want.txt", "w") as f:
    f.write("Hello darkness my old friend")
   
with open("/home/robuntu/Sairam/ICS4U-Classwork/learning_python/Tell me what u want.txt", "r") as f:
    bob = f.read()

f = open("bob.txt", "w")
f.write("Manually opening and closing. the 'with' automatically closes")
f.close()
blip = os.path.abspath("writing_files.py")

# Converting data
# data must be written as a string
# and must be converted back to the desired
# datatype once read.
with open("some_file.txt", 'w') as f:
    f.write(str(100))

with open("some_file.txt", 'r') as f:
    value = int(f.read())

print(value * 2)

# Create 100 files called file{num}.txt
# put "hello" in each file
for n in range(100):
    with open(f"file{n}.txt", 'w') as f:
        f.write("Hello")

# Remove all files in the directory that start with 'file'
import os

file_list = os.listdir()

for name in file_list:
    if name.startswith('file'):
        os.remove(name)

print(blip)
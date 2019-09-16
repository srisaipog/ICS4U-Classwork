# Writing Files

import os

with open("/home/robuntu/Sairam/ICS4U-Classwork/learning_python/Tell me what u want.txt", "w") as f:
    f.write("Hello darkness my old friend")
   
with open("/home/robuntu/Sairam/ICS4U-Classwork/learning_python/Tell me what u want.txt", "r") as f:
    bob = f.read()

blip = os.path.abspath("writing_files.py")

print(blip)
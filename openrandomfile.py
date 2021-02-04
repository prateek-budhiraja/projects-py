import random
import os

pth='/home/prateek/Pictures/college'
os.chdir(pth)
# randomly selecting a file
filename=random.choice(os.listdir())
print("Enjoy!")
# command to open a file with it's default application
os.system("xdg-open "+filename)

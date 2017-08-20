import os 
import sys
import shutil


for i in range(1,3):
    if not os.path.exists('./rech{0}'.format(i)):
            os.mkdir('./rech{}'.format(i))
    for j in range(0,10):
        if not os.path.exists('./rech{0}/{1:02d}.py'.format(i,j)):
            shutil.copyfile('./00.py', './rech{0}/{1:02d}.py'.format(i,j))



# Objective: Implement time out
# @Author:  Aseem Jain
# @Github: https://github.com/premaseem

import datetime
from time import sleep

import time

init_time = time.time()
print(init_time)
sleep(2)
current_time = time.time()


if current_time - init_time >  10:
    print ("Time has passed.")
else:
    print("still working")

#sleep(30)


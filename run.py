# run.py
from auto_labeling import *

user_name = "蛤"
iter_num = 5

L = Naive_Label_Client(user_name)
L.run(iter_num)
import os
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

FILE_PATH = os.path.dirname(__file__)
DATA_PATH = os.path.join(FILE_PATH, 'en-th.yml')

with open(DATA_PATH, 'r') as file:
    en_th = load(file)

    text = "l;ylfu8iy["
    decode = ""
    for t in text:
        decode += en_th[t]

    print(decode)
    print(en_th)
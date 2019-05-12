import os
from yaml import load, dump
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

FILE_PATH = os.path.dirname(__file__)
DATA_PATH = os.path.join(FILE_PATH, 'en-th.yml')

with open(DATA_PATH, 'r') as file:
    en_th = load(file)

    text = input("Enter text to Convert: ")
    decode = ""
    for t in text:
        decode += en_th[t]

    print(decode)
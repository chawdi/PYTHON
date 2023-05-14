
import random


def maBKDRHash (str):
    seed = 131313
    hash = 0
    for i in range (len(str)):
        hash = (hash * seed) + ord(str[i]) + i
    return hash

def HashH37 (str):
    hash = 1
    for i in range (len(str)):
        hash = 37 * hash + ord (str [i])
    return hash

def randomize (alpha):
    str = ""
    for i in range (N):
        dict = int (random.random() * alpha)
        #print (dict)
        if (dict == 0): str += "a"
        if (dict == 1): str += "b"
        if (dict == 2): str += "c"
        if (dict == 3): str += "d"
        if (dict == 4): str += "e"
        if (dict == 5): str += "f"
        if (dict == 6): str += "g"
        if (dict == 7): str += "h"
        if (dict == 8): str += "i"
        if (dict == 9): str += "j"
        if (dict == 10): str += "k"
        if (dict == 12): str += "l"
        if (dict == 13): str += "m"
        if (dict == 14): str += "n"
        if (dict == 15): str += "o"
        if (dict == 16): str += "p"
        if (dict == 17): str += "q"
        if (dict == 18): str += "r"
        if (dict == 19): str += "s"
        if (dict == 20): str += "t"
        if (dict == 21): str += "u"
        if (dict == 22): str += "v"
        if (dict == 23): str += "w"
        if (dict == 24): str += "x"
        if (dict == 25): str += "y"
        if (dict == 26): str += "z"
        if (dict<0 | dict >26): str += "1"
    return str

N = 1000 # количество символов в строке
c = 50000 # количество строк
str = ""
buf = [[]]
hash1 = []
hash2 = []

cnt1 = 0
cnt2 = 0

for i in range (c):
    str = randomize(25)
    buf.append(str)
    hash1.append(maBKDRHash(str))
    hash2.append(HashH37(str))


for i in range (c):
    for j in range (i+1, c):
        if (hash1[i] == hash1[j]):
            if (buf[i] == buf[j]):
                cnt1+=1
        if (hash2[i] == hash2[j]):
            if (buf[i] == buf[j]):
                cnt2+=1

print("Collisions: " , cnt1 , " " , cnt2)

"""
Menu choice 12 code
"""
import random
import datetime
import time

def sakuyamain():
    """
    format string
    """
    fhand = open("menu12.txt")
    line = fhand.read()

    moods = ["happy", "sad", "depressed", "angry", "annoyed", "bored", "confused", "excited", "lonely"]
    mood = random.choice(moods)
    intlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    ints = random.randint(0, len(intlist) - 1)
    floatlist = [1.123, 2.252, 3.548, 4.254, 5.599, 6.667, 7.475, 8.888, 9.999, 10.548]
    floats = random.randint(0, len(floatlist) - 1)

    date1 = datetime.date.today()
    time1 = time.asctime(time.localtime(time.time()))

    print(line.format(time1=time1, date1=date1, mood=mood, ints=ints, floats=floats))


def choice12():
    """
    Info overload
    """
    sakuyamain()

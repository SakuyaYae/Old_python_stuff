"""
Plane hight, speed and tempratur calkulation
"""

meters = float(input("type hight over the sea in meters "))

speed_kh = float(input("type how fast you are flying in k/h "))

tempratur_c = float(input("type what tempratur it is out side in C "))


feet = meters * 3.28084
print(feet)

speed_mph = speed_kh * 0.62137
print(speed_mph)

tempratur_f = (((tempratur_c * 9) / 5) + 32)
print(tempratur_f)

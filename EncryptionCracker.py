import string
from random import randint
from time import sleep
import sys

encryption = input("enter what you want to decrypt:\n")

rand = randint(1, 100)
roll_chance = randint(1, 10000)
z = 5
for i in range(20):
    sys.stdout.write("\rDecrypting: " + str(z) +"%")
    z += 5
    sleep(1)
if rand == 100:
    sys.stdout.write("Decryption failed, exiting")
    exit("Error Code: " + str(randint(1, 1000)))
elif roll_chance == 9999:
    from webbrowser import open as webopen
    webopen("https://m.youtube.com/watch/dQw4w9WgXcQ", new = 2)
else:
    for j in range(10000):
        print(str(hex(random.randint(0, 255))), end = '')
        sleep(0.001)
    count = random.randint(5, 35)
    letters = string.ascii_letters
    sys.stdout.write("\nDecryption successful, result is:\n")
    sys.stdout.write(''.join(random.choice(letters) for i in range(count)))

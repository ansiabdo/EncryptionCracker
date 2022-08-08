import string
import random
import time
import sys

encryption = input("enter what you want to decrypt:\n")

rand = random.randint(1, 100)
rando = random.randint(1, 1000)
z = 5
for i in range(20):
    sys.stdout.write("\rDecrypting: " + str(z) +"%")
    z += 5
    time.sleep(1)
if rand == 100:
    sys.stdout.write("Decryption failed, exiting")
    exit("Error Code: " + str(rando))
else:
    for j in range(10000):
        print(str(hex(random.randint(0, 255))), end = '')
    count = random.randint(5, 35)
    letters = string.ascii_letters
    sys.stdout.write("\nDecryption successful, result is:\n")
    sys.stdout.write(''.join(random.choice(letters) for i in range(count)))

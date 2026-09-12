import time

a, b = 1000, 7
while a >= 7:
    print(f"{a} - {b} = {a - b}")
    a -= b
    time.sleep(0.1)
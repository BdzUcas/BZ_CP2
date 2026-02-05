#https://28rolfsonbisppedukh.itch.io/space-simulator
import time as t
height = 0

while not False:
    print('#')
    for i in range(height):
        print()
    increase = input()
    height = height + 1
    print("\033c", end="")
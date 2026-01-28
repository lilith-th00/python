import sys
import math

def distance(cord1, cord2):
    totale = 0
    for i in range(len(cord1)):
        totale += (cord2[i] - cord1[i]) ** 2
    return math.sqrt(totale)
print("=== Game Coordinate System ===\n")

my1_tuple = (10, 20, 5)
my2_tuple = (0, 0, 0)
print(f"Position created: {my1_tuple}")
print(f"Distance between {my2_tuple} and {my1_tuple}: {distance(my1_tuple, my2_tuple):.2f}")
print()

cord = "3,4,0"
my_tuple = tuple(int(x) for x in cord.split(","))
print(f'Parsing coordinates: "{cord}"')
print(f"Parsed position: {my_tuple}")
print(f"Distance between {my2_tuple} and {my_tuple}: {distance(my_tuple, my2_tuple):.1f}")
print()
cord = "abc,def,ghi"
try:
    for x in cord.split(","):
        c = x
        my_tuple = tuple(int(x))
except ValueError as e:
    print(f'Parsing invalid coordinates: "{cord}"')
    print(f"Error parsing coordinates: invalid literal for int() with base 10: '{c}'")
    print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
print()

x, y, z = my1_tuple
print("Unpacking demonstration:\n")
print(f"Player at x={x}, y={y}, z={z}")
print(f"Coordinates: X={x}, Y={y}, Z={z}")
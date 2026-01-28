import sys

n = len(sys.argv)
print("=== Command Quest ===")
if n == 1:
    print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    print(f"Total arguments: {n}")
else:
    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments received: {n - 1}")
    for i in range(1, n):
        print(f"Argument {i}: {sys.argv[i]}")
    print(f"Total arguments: {n}")
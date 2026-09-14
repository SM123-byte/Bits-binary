input("Parity - last bit = 0 even, last bit = 1 odd. Press enter: ")

for n in [2, 3, 4, 5, 8, 9]:
    if n & 1:
        print(" ", n, "-> odd")
    else:
        print(" ", n, "-> even")

n = int(input("Enter a number (try 13 or 7): "))
input("Counts the 1s - watch the bits drop off. Press enter ")
temp = n
while temp > 0:
    print(" binary:", bin(temp)[2:], "  last bit:", temp & 1)
    temp >>= 1
print("  total is in", n, "=", bin(n).count('1'))
n = int(input("Enter a number (try 5 or 12): "))
guess = input("Guess its binary number: ")

input("Binary. Press enter to see the binary number: ")
print("\ndecimal", n, "-> binary", bin(n)[2:])
print(" your guess:", guess)

input("AND - both bits must be 1. Press enter: ")
print(" 12=", bin(12)[2:])
print(" 10=", bin(10)[2:])
print(" 12 & 10 = ", 12 & 10)

input("OR - at least one bit must be one. Press enter: ")
print(" 12 | 10 = ", 12 | 10)
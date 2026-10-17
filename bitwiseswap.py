print("BITWISE SWAP CHALLENGE")

a, b = 56, 12
print("\nPART 1: Swap Without a Third Variable")
print("Before Swap:\na =", a, "\nb =", b)

a = a + b
b = a - b
a = a - b
print("After Swap:\na =", a, "\nb =", b)

x, y = 45, 18
print("\nPART 2: XOR Swap")
print("Before XOR Swap:\nx =", x, "\ny =", y)

x = x ^ y
y = x ^ y
x = x ^ y
print("After XOR Swap:\nx =", x, "\ny =", y)

number = 3
print("\nPART 3: Left Shift Doubles the Number")
print("Original Number:", number)
print(number, "<< 1 =", number << 1)
print(number, "<< 2 =", number << 2)
print(number, "<< 3 =", number << 3)
print(number, "<< 4 =", number << 4)
print("Each left shift multiplies the number by 2.")

num1, num2 = -10, 5
print("\nPART 4: XOR for Sign Detection")
print("num1 =", num1, "\num2 =", num2)

if (num1 < 0) ^ (num2 < 0):
    print("The numbers have different signs.")
else:
    print("The numbers have the same sign.")

dividend, divisor = 25, 4
quotient, remainder = 0, dividend

while remainder >= divisor:
    remainder = remainder - divisor
    quotient = quotient + 1

print("\nPART 5: Divide Without /")
print("Dividend:", dividend, "\nDivisor:", divisor)
print("Quotient:", quotient, "\nRemainder:", remainder)

print("BITWISE SWAP CHALLENGE SUMMARY")
print("Swap without third variable uses addition and subtraction.")
print("XOR swap uses the ^ operator to swap values.")
print("Left shift doubles a number.")
print("XOR can help detect different signs.")
print("Division can be done using repeated subtraction.")
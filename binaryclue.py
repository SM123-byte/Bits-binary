print("===\nBINARY CLUE\n===")

a, b = 7, 7
print(f" PART 1: XOR Identity and Equality\na = {a}\nb = {b}\na ^ a = {a ^ a}\na ^ 0 = {a ^ 0}")
print("Both numbers are equal" if (a ^ b) == 0 else "Both numbers are different")

clues = [3, 5, 3, 5, 9]
xor_result = 0
for c in clues: xor_result ^= c
print(f"\n PART 2: XOR Cancellation\nClues: {clues}\nFinal XOR Result: {xor_result}\nRepeated clues cancel out, so the remaining clue is: {xor_result}")

numbers = [4, 7, 4, 2, 7, 2, 9]
odd_number = 0
for n in numbers: odd_number ^= n
print(f"\n PART 3: One Odd-Occurring Number\nNumbers: {numbers}\nOdd-occurring number: {odd_number}")

pair_numbers = [3, 9, 3, 5, 5, 7]
xor_of_two = 0
for n in pair_numbers: xor_of_two ^= n

rightmost_set_bit = xor_of_two & -xor_of_two
first_odd = second_odd = 0
for n in pair_numbers:
    first_odd ^= n if (n & rightmost_set_bit) else 0
    second_odd ^= 0 if (n & rightmost_set_bit) else n

print(f"\n PART 4 & 5: Two Odd-Occurring Numbers\nNumbers: {pair_numbers}\nXOR of two: {xor_of_two}\nRightmost set bit: {rightmost_set_bit}\nFirst odd: {first_odd}\nSecond odd: {second_odd}")

# FINAL SUMMARY
print(f"""
===BINARY CLUE INVESTIGATION SUMMARY=== XOR Identity: a ^ a = 0 XOR with zero: a ^ 0 = a XOR Cancellation removes repeated pairs One odd-occurring number found: {odd_number} Two odd-occurring numbers found:{first_odd} and {second_odd}""")
print("==\nPOWER OF TWO SCANNER\n===")

n = 16
print(f"\nPART 1: The n & (n-1) Trick\nn = {n} -> {bin(n)}\nn - 1 = {n - 1} -> {bin(n - 1)}\nn&(n-1) = {n & (n - 1)} -> {bin(n & (n - 1))}\n\nThis trick removes the rightmost set bit.")

def is_power_of_2(num):
    return num > 0 and (num & (num - 1)) == 0

def check_power(num, base_log):
    if not is_power_of_2(num): return False
    
    position = 0
    while num > 1:
        num >>= 1
        position += 1
    return position % base_log == 0

numbers = [1, 2, 4, 6, 8, 12, 16, 18, 32]

print("\nPART 2: Power of 2 Check")
for num in numbers:
    print(f"{num} -> {bin(num)} -> {is_power_of_2(num)}")

print("\nPART 3: Power of 4 Check")
for num in numbers:
    print(f"{num} -> {check_power(num, 2)}")

print("\nPART 4: Power of 8 Check")
for num in numbers:
    print(f"{num} -> {check_power(num, 3)}")

def binary_power(base, exponent):
    answer = 1
    while exponent > 0:
        if exponent & 1: answer *= base
        base *= base
        exponent >>= 1
    return answer

print(f"\nPART 5: Binary Exponentiation\n2^5 = {binary_power(2, 5)}\n3^4 = {binary_power(3, 4)}\n5^3 = {binary_power(5, 3)}")

print("""
POWER SCANNER SUMMARY
Power of 2: only one bit is set.
Power of 4: set-bit position is even.
Power of 8: set-bit position is divisible by 3.
Binary exponentiation calculates powers quickly.
""")

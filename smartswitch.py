switch_value = 45 
switches = ["Living Room Light", "Fan", "Air Conditioner", "Door Lock", "Garden Light", "Security Camera"]
binary = f"{switch_value:06b}"

print(f"===\nMY SMART SWITCH BIT MONITOR\n====\nSwitch Value: {switch_value}\nBinary Form: {binary}")
print(f" PART 1: Set Bits and Zero Bits\nSet Bits / ON Switches: {binary.count('1')}\nZero Bits / OFF Switches: {binary.count('0')}") # Categorise both the off and on switches

on_count = bin(switch_value).count("1")
first_on = (switch_value & -switch_value).bit_length()
print(f" PART 2: Counting Set Bits\nNumber of ON switches: {on_count}") # total active switches in line above
print(f" PART 3: The First Set Bit\nFirst ON switch is at position: {first_on}") #displays frst active position in line above

print(" PART 4: Building a Bit Mask") # Ready to mask
for i in range(6):
    print(f"Bit {i} Mask: {1 << i} Binary: {1 << i:b}")

print(" PART 5: Check if the Nth Bit is Set")
for i, name in enumerate(switches):
    status = "ON" if switch_value & (1 << i) else "OFF" # Checks if the bit is ON or OFF
    print(f"Bit {i} - {name} is {status}")

print(f" ===\nSMART SWITCH SUMMARY\n===\nSwitch Value: {switch_value}\nBinary Form: {binary}\nTotal ON Switches: {on_count}\nFirst ON Switch Position: {first_on}\n===")

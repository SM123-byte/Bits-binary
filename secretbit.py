secret_code, access_key = 13, 9

def bits(num, w=4):
    return format(num & ((1 << w) - 1), f"0{w}b")

print(f"Secret: {secret_code} ({bits(secret_code)})")
print(f"Access: {access_key} ({bits(access_key)})\n--- Operations ---")

and_res, or_res, xor_res = (
    secret_code & access_key,
    secret_code | access_key,
    secret_code ^ access_key,
)
not_res, l_shift, r_shift = (~secret_code) & 15, secret_code << 1, secret_code >> 1

print(f"AND: {and_res} ({bits(and_res)})  | OR: {or_res} ({bits(or_res)})")
print(f"XOR: {xor_res} ({bits(xor_res)})  | NOT (4-bit): {not_res} ({bits(not_res)})")
print(f"L-Shift: {l_shift} ({bits(l_shift, 5)}) | R-Shift: {r_shift} ({bits(r_shift)})")

is_odd = "Odd" if (secret_code ^ 1) == secret_code - 1 else "Even"
print(f"\nProperties:\n- Code is {is_odd} (via XOR 1 check)")
print(f"- Set bits (1s) count: {secret_code.bit_count()}")
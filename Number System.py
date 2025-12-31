def convert_to_base(num, base):
    # Characters for digits up to base 36
    digits_map = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Handle zero as a special case
    if num == 0:
        return "0"

    digits = []
    temp = num
    while temp > 0:
        remainder = temp % base
        digits.append(digits_map[remainder])  # Use digit or letter
        temp //= base

    # Reverse to get correct order
    digits.reverse()
    return ''.join(digits)


# Main program
num = int(input("Enter a number: "))
base = int(input("Enter the base (2–36): "))

if base < 2 or base > 36:
    print("Base must be between 2 and 36")
else:
    converted = convert_to_base(num, base)
    print(f"The number {num} in base {base} is: {converted}")



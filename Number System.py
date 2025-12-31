def convert_to_base(num, base):
    digits_map = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   
    if num == 0:
        return "0"

    is_negative = num < 0
    num = abs(num)

    digits = []
    temp = num
    while temp > 0:
        remainder = temp % base
        digits.append(digits_map[remainder]) 
        temp //= base

    digits.reverse()
    result = ''.join(digits)

    if is_negative:
        result = "-" + result

    return result


# Main program
num = int(input("Enter a decimal number: "))
base = int(input("Enter the base (2–36): "))

if base < 2 or base > 36:
    print("Base must be between 2 and 36")
else:
    converted = convert_to_base(num, base)
    print(f"The number {num} in base {base} is: {converted}")

#Output
Enter a decimal number: -23456
Enter the base (2–36): 16
The number -23456 in base 16 is: -5BA0


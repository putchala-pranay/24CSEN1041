password = input("Enter a password: ")

length_ok = len(password) >= 8
has_digit = any(ch.isdigit() for ch in password)
has_upper = any(ch.isupper() for ch in password)
has_lower = any(ch.islower() for ch in password)
has_special = any(ch in "!@#$%^&*()-_=+[]{};:,.<>?/\\|" for ch in password)

if length_ok and has_digit and has_upper and has_lower and has_special:
    print("Strong password ")
elif length_ok and (has_digit or has_special) and (has_upper or has_lower):
    print("Medium password ")
else:
    print("Weak password ")

OUTPUT:
Enter a password: pasword@11D
Strong password 

Method-1:

text = input("Enter a Word:")
reversing = reversed(text)
reversed_text="".join(reversing)
if text == reversed_text:  
    print("Palindrome")
else:
    print("Not a Palindrome")

Method-2:
text = input("Enter a Word:")
if text = text[::-1]:  
    print("Palindrome")
else:
    print("Not a Palindrome")


OUTPUT:
Enter a Word:RACECAR
Palindrome

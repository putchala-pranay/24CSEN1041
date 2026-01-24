text = input("Enter a Word:")
reversing = reversed(text)
reversed_text="".join(reversing)
if text == reversed_text:  
    print("Palindrome")
else:
    print("Not a Palindrome")

OUTPUT:
Enter a Word:RACECAR
Palindrome

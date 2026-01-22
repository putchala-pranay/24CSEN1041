string = input("Enter a string:")
text = reversed(string)
reversed_text="".join(text)
print("Reversed string:", reversed_text)
______________________________________
text = input("Enter a string: ")
reversed_text = ""
i = len(text) - 1
while i >= 0:
    reversed_text += text[i]
    i -= 1
print("Reversed string:", reversed_text)
________________________________________

Output:
Enter a string:programing
Reversed string: gnimargorp

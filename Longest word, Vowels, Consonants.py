sentence = input("Enter a string:")
text = sentence.lower()
words = sentence.split()
longest = max(words, key=len)
vowels = "aeiou"
v_count = sum(1 for ch in text if ch in vowels)
c_count = sum(1 for ch in text if ch.isalpha() and ch not in vowels)

print("Vowels:", v_count)
print("Consonants:", c_count)
print("Longest word:", longest)

OUTPUT:
Enter a string: Hi my name is Pranay
Vowels: 6
Consonants: 10
Longest word: Pranay

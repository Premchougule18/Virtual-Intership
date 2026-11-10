text = input("Enter a word: ")

reverse = text[::-1]

if text == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")
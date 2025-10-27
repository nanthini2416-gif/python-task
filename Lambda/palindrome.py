words = ["level", "hello", "radar", "world", "madam"]


is_palindrome = lambda word: word == word[::-1]


for word in words:
    if is_palindrome(word):
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")

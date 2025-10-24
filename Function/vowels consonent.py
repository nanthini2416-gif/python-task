def count_chars(s):
    
    vowels = 0
    consonants = 0
    special = 0
    for c in s:
        if c.lower() in 'aeiou':
            vowels += 1
        elif c.isalpha():
            consonants += 1
        else:
            special += 1
    print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("Special characters:", special)

count_chars("Hi! How are you?")


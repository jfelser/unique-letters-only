import os

# Open the file
module_dir = os.path.dirname(__file__)
WORD_LIST = os.path.join(module_dir, "sowpods.txt")
wordlist = open(WORD_LIST).readlines()

# Get rid of newlines
wordlist = [word.lower().strip() for word in wordlist]

# Track a few things
words_without_vowels = []
longest_word = []
longest_word_length = 0

# Decide if a word uses only unique letters
def is_unique(word):
    letters = list(word)
    unique_letters = set(letters)

    if len(letters) == len(unique_letters):
        return True

    return False

# Decide if a word has a vowel
def has_vowel(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    for vowel in vowels:
        if list(word).count(vowel) > 0:
            return True

    return False

# Decide if a word is the longest
def is_longest(word):
    global longest_word_length, longest_word

    if len(word) == longest_word_length:
        longest_word.append(word)
    
    elif len(word) > longest_word_length:
        longest_word = [word]
        longest_word_length = len(word)

# Check if the words use only unique letters
unique_words = 0
unique_words_with_vowel = 0

for word in wordlist:
    if is_unique(word):
        if has_vowel(word):
            unique_words_with_vowel += 1
        else:
            words_without_vowels.append(word)
        
        is_longest(word)
        unique_words += 1

# Print outcome
print('Total number of words in word list: {}'.format(len(wordlist)))
print('Number of words using each letter at most once: {}'.format(unique_words))
print('Number of words using each letter at most once, with a vowel: {}'.format(unique_words_with_vowel))
print('Words using each letter at most once, without a vowel: {}'.format(words_without_vowels))
print('Longest word length: {}'.format(longest_word_length))
print('Longest word(s): {}'.format(longest_word))
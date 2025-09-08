"""
Spellchecker
------------
This program checks a given text against a wordlist and marks misspelled words.

Functions:
- wordlist(): reads words from "wordlist.txt" ans saves them in a new list
- find(text, new_list): compare words from the input text with the new_list and highlights unknown words with asterisks
"""
text = str(input("Write text: "))

def wordlist():
    with open("wordlist.txt") as new_file:
        new_list = []
        for line in new_file:
            parts = line.strip()
            new_list.append(parts)
    return new_list

def find(text, new_list):
    new_text = []
    words = text.split()
    for word in words:
        lower_word = word.lower()
        if lower_word in new_list:
            new_text.append(word)
        else: 
            new_text.append(f"*{word}*")
    return " ".join(new_text)

new_list = wordlist()
print(find(text, new_list))

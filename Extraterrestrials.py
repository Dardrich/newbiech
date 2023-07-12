# You meet a group of aliens, and their language is just like English except that they say every words backwards. 
# Task: Take a word in English and reverse it

human_words = str(input("Enter the words that you want me to translate: "))

for i in human_words.split():
    print(i[::-1])
    if human_words == i[::-1]:
        print("Wow, that's a palindrome!")
    else:
        continue
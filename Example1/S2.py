list_of_words = ["hello", "yes", "goodbye","last",""]
total_word= ""

for i in range(4): # len(list_of_words)
    total_word += list_of_words[i]
    if i !=3:  #len(list_of_words) -1:
        total_word += ".."
print(total_word)

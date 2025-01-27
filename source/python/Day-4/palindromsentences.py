def is_palindrome(word):
    return word == word[::-1]

def remove_space(sentence):
    words = []
    word = ""
    for char in sentence:
        if char != ' ':
            word += char
        else:
            if word:
                words.append(word)
                word = ""
    if word:
        words.append(word)
    
    palindrome_words = []
    for word in words:
        if is_palindrome(word):
            palindrome_words.append(word)
    
    pal_words = ""
    for word in palindrome_words:
        if pal_words:
            pal_words += " "
        pal_words += word
    
    return pal_words

sentence = "the    boy  is using  radar with   level in the forest of   madam"
pal_words = remove_space(sentence)
print(pal_words)  


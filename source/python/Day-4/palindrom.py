def is_palindrome(string):
    return string == string[::-1]

def find_palindromes(words):
    return [word for word in words if is_palindrome(word)]

words = ["radar", "hello", "level", "world", "madam"]
palindromes = find_palindromes(words)
print(palindromes) 
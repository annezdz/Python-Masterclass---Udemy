def multiply(x: float, y: float) -> float:
    result = x * y
    return result


answer = multiply(2.5, 2)
print(answer)

for val in range(1, 5):
    two_times = multiply(2, val)
    print(two_times)


def is_palindrome(string: str) -> bool:
    return string[::-1] == string.casefold(),


word = input("Please enter a word to check:".casefold())
if is_palindrome(word):
    print('{} is a palindrome'.format(word))
else:
    print('{} is not a palindrome'.format(word))


def palindrome_sentence(string:str) -> bool:
    filtered_string = ''.join(filter(str, string)).casefold()
    if filtered_string[::-1] == string.casefold():
        return True
    else:
        return False


def palindrome(sentence):
    string = ''
    for char in sentence:
        if char.isalnum():
            string += char
    if string[::-1] == sentence.casefold():
        return True
    else:
        return False


name = 'Ana'
teste = '##d*+'
print(palindrome_sentence('Madam'))
print(palindrome_sentence('Civic'))
print(palindrome_sentence('Level'))
print(palindrome_sentence('Tenet'))
print(palindrome_sentence('Malayalam'))
print(palindrome_sentence('Noon'))
print(palindrome_sentence('Edu'))
print(palindrome_sentence('123'))
print(palindrome_sentence('12321'))
print(palindrome_sentence('123321'))

print()
print(palindrome_sentence('2422442551'))

print(palindrome_sentence(name))


p = palindrome_sentence()
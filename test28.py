def reverse_words(text):
    return ' '.join(map(lambda x: x[::-1], text.split(' ')))








res = reverse_words('The quick brown fox jumps over the lazy dog.')
print(res)

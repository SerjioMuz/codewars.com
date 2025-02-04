def alphabet_position(text):
    return ' '.join([str(ord(i)-96) for i in text.lower() if 'a'<=i<='z'])






res = alphabet_position("AaThe sunset sets at twelve o' clock.")
print(res)
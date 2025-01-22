text='Python is Python and again Python'
text2=text.split()
text3=''
for i in text2:
    if i not in text3:
        text3 = text3 + i+' '
print(text3)

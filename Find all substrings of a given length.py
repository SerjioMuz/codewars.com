text='Python'
text3=[]
j=int(input('Введите оличество символов'))
for i in range((len(text)-(j-1))):
    text2=text[i:(i+j)]
    print(text2)
    text3=text3+[text2]
print(text3)
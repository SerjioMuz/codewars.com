from collections import Counter
text='programmingg'
text2=Counter(text)
print(text2)
#res = list(text2.items())[0]
#print(res)
#print(max(text2.values()))
#print('самый встречающийся элемент', (list(text2.keys())[0]))
print('самый встречающийся элемент',max(text2, key=text2.get))

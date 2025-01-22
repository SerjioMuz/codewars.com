text='Pythonskljhlkgjjljhfhjdsjdhgdtyedutrskhgdkdkf    kf k      '
text.lower()
q=''
w=''
for i in text:
    var = i in ("aeiouy")
    print(var)
    if var:
        q+=i
    else:
        w+=i
print(len(q), len(w))

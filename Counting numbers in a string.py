text='In 2023 I earned 1500 hryvnia'
text2=text.split()
dij=0
for i in text2:
    if i.isdigit():
        dij=dij+int(i)

return(dij)

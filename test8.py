def abbrev_name(name):
    return (name[0]+'.'+name[name.find(' ')+1]).title()










res = abbrev_name('jon smit')
print(res)
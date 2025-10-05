"Exercise 1 Поиск самого крупного файла с исходным кодом Python в отдельно взятом каталоге"
import os, glob
dirname=r'C:\Users\Serjio2\AppData\Local\Programs\Python\Python313\Lib'
allsize=[]
allpy=glob.glob(dirname + os.sep+'*.py')
for filename in allpy:
    filesize=os.path.getsize(filename)
    allsize.append((filesize, filename))
allsize.sort()
print(allsize[:2])
print(allsize[-2:])

"Exercise 2 Поиск самого крупного файла с исходным кодом Python в дереве каталогов"
import sys, os, pprint
if sys.platform[:3]=='win':
    dirname=r'C:\Users\Serjio2\AppData\Local\Programs\Python\Python313\Lib'
else:
    dirname='/usr/lib/python'
allsize=[]
for (thisDir, subsHere, filesHere) in os.walk(dirname):
    for filename in filesHere:
        if filename.endswith('.py'):
            fullname=os.path.join(thisDir, filename)
            fullsize=os.path.getsize(fullname)
            allsize.append((fullsize, fullname))
allsize.sort()
pprint.pprint(allsize[:2])
pprint.pprint(allsize[-2:])

"Exercise 2 Поиск самого крупного файла с исходным кодом Python в пути поиска импортируемых модулей"
import sys, os, pprint
visited={}
allsizes=[]
for crsdir in sys.path:
    for (thisDir, subsHere, filesHere) in os.walk(crsdir):
        thisDir=os.path.normpath(thisDir)
        if thisDir.upper() in visited:
            continue
        else:
            visited[thisDir.upper()]=True
        for filename in filesHere:
            if filename.endswith('.py'):
                pypath=os.path.join(thisDir, filename)
                try:
                   pysize=os.path.getsize(pypath)
                except:
                   print('skipping', pypath)
                allsizes.append((pysize, pypath))
allsizes.sort()
pprint.pprint(allsizes[:3])
pprint.pprint(allsizes[-3:])

"Exercise 3 Суммирование столбцов в текстовом файле с разделителями-запятыми"
filename='data.txt'
sums={}
for line in open(filename):
    cols=line.split(',')
    nums=[int(col) for col in cols]
    for (ix, num) in enumerate(nums):
        sums[ix]=sums.get(ix,0)+num
for key in sorted(sums):
    print(key, '=', sums[key])

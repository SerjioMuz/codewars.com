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


"Exercise 4 Суммирование столбцов в текстовом файле с разделителями-запятыми, списки вместо словарей"
import sys
filename = sys.argv[1]
numcols=int(sys.argv[2])
totals=[0]*numcols
for line in open(filename):
    cols=line.split(',')
    nums=[int(x) for x in cols]
    totals=[(x+y) for (x,y) in zip(totals, nums)]
print(totals)


"Exercise 5 Проверка возвращения в предыдущее состояние вывода для набора сценариев"
import os
testscripts=[dict(script='test1.py', args=''),
dict(script='test2.py', args='spam')]
for testcase in testscripts:
    commandline='%(script)s %(args)s' % testcase
    output=os.popen(commandline).read()
    result=testcase['script']+'.result'
    if not os.path.exists(result):
        open(result, 'w').write(output)
        print('Created:', result)
    else:
        priorresult=open(result).read()
        if output != priorresult:
            print('FAILED:', testcase['script'])
            print(output)
        else:
            print('Passed:', testcase['script'])


"Exercise 6 Построение графического пользовательского интерфейса"
from tkinter import *
import random
import pygame
import datetime

pygame.mixer.init()
fontsize = 25
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'white', 'cyan', 'purple']


def reply(text):
    print(text)
    popup = Toplevel()
    color = random.choice(colors)
    Label(popup, text='Popup', bg=random.choice(colors), fg=color).pack()
    L.config(fg=color)


def timer():
    L.config(fg=random.choice(colors))
    win.after(250, timer)


def grow():
    global fontsize
    fontsize += 1
    L.config(font=('arial', fontsize, 'italic'))
    win.after(100, grow)


def sound():
    sound = pygame.mixer.Sound('C:\Alarm09.wav')
    sound.play()


def datatime():
    datatime = Toplevel()
    color = 'red'
    Label(datatime, text=datetime.datetime.now(), bg='blue', fg=color).pack()
    L.config(fg=color)


win = Tk()
L = Label(win, text='ПРИВЕТrrrrrr',
          font=('tahoma', fontsize, 'italic'), fg='yellow', bg='navy',
          relief=RAISED)
L.pack(side=TOP, expand=YES, fill=BOTH)
Button(win, text="press", command=(lambda: reply('red'))).pack(side=BOTTOM, fill=X)
Button(win, text='timer', command=timer).pack(side=BOTTOM, fill=X)
Button(win, text='grow', command=grow).pack(side=BOTTOM, fill=X)
Button(win, text='sound', command=sound).pack(side=BOTTOM, fill=X)
Button(win, text='datatime', command=datatime).pack(side=BOTTOM, fill=X)

win.mainloop()


"Exercise 6 Построение графического пользовательского интерфейса с использованием классов"
from tkinter import *
import random
import pygame
import datetime

pygame.mixer.init()


class MyGui:
    colors = ['red', 'green', 'blue', 'yellow', 'orange', 'white', 'cyan', 'purple']

    def __init__(self, parent, title='popup'):
        parent.title(title)
        self.growing = False
        self.fontsize = 10
        self.lab = Label(parent, text='Guil', fg='white', bg='navy')
        self.lab.pack(expand=YES, fill=BOTH)
        Button(parent, text='Spam', command=self.reply).pack(side=LEFT)
        Button(parent, text='Grow', command=self.grow).pack(side=LEFT)
        Button(parent, text='Stop', command=self.stop).pack(side=LEFT)
        Button(parent, text='Sound', command=self.sound).pack(side=LEFT)

    def reply(self):
        self.fontsize += 5
        color = random.choice(self.colors)
        self.lab.config(bg=color, font=('courier', self.fontsize, 'bold italic'))

    def grow(self):
        self.growing = True
        self.grower()

    def grower(self):
        if self.growing:
            self.fontsize += 5
            self.lab.config(font=('courier', self.fontsize, 'bold'))
            self.lab.after(500, self.grower)

    def sound(self):
        sound = pygame.mixer.Sound('C:\Alarm09.wav')
        sound.play()

    def stop(self):
        self.growing = False


class MySubGui(MyGui):
    colors = ['black', 'purple']

    def grower(self):
        if self.growing:
            self.fontsize += 20
            self.lab.config(font=('courier', self.fontsize, 'bold'))
            self.lab.after(500, self.grower)

    def sound(self):
        sound = pygame.mixer.Sound('C:\Alarm08.wav')
        sound.play()


class MySubCui2(MyGui):
    def __init__(self, parent, title='tttttt'):
        self.growing = False
        self.fontsize = 10
        self.lab = Label(parent, text='Guil', fg='white', bg='navy')
        self.lab.pack(expand=YES, fill=BOTH)
        Button(parent, text='datatime', command=self.datatime).pack(side=LEFT)
        Button(parent, text='Spam', command=self.reply).pack(side=LEFT)
        Button(parent, text='Grow', command=self.grow).pack(side=LEFT)
        Button(parent, text='Stop', command=self.stop).pack(side=LEFT)
        Button(parent, text='Sound', command=self.sound).pack(side=LEFT)

    def datatime(self):
        datatime = Toplevel()
        color = 'red'
        Label(datatime, text=datetime.datetime.now(), bg='blue', fg=color).pack()


MyGui(Tk(), 'main')
MyGui(Toplevel())
MySubGui(Toplevel(), 'eeeee')
MySubCui2(Toplevel(), 'yyyyy')
mainloop()


"Exercise 7 Утилита для просмотра и обслуживания входящих сообщений электронной почты"

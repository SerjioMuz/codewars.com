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
import imaplib, getpass, sys
mailserver='imap.ukr.net'
mailuser='muzikant_s_v@ukr.net'
mailpassword=getpass.getpass('Password for %s?' % mailserver)

print('Connecting...')
server=imaplib.imap(mailserver)
server.user(mailuser)
server.pass_(mailpassword)

try:
    print(server.getwelcome())
    msgCount, mboxSize=server.stat()
    print('There are', msgCount, 'mail messages, size', mboxSize)
    msginfo=server.list()
    print(msginfo)
    for i in range(msgCount):
        msgnum=i+1
        msgsize=msginfo[1][i]
        resp, hdrlines,octets=server.top(msgnum, 0)
        print('-'*80)
        print('[%d: octets=%d, size=%s]' % (msgnum, octets, msgsize))
        for line in hdrlines: print(line)
        if input ('Print') in ['y','Y']:
            for line in server.retr(msgnum)[1]: print(line)
        if input('Delete') in ['y','Y']:
            print('Deleting')
            server.dele(msgnum)
        else:
            print('Skipping')
finally:
    server.quit()
input('Bye.')


"Exercise 8 Серверный сценарий CGI для взаимодействия с веб-браузером"
#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Отправляем форму пользователю
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"""
            <html>
            <head><title>Reply Page</title></head>
            <body>
                <form method="POST">
                    <label>Enter your name:</label>
                    <input type="text" name="user">
                    <input type="submit" value="Send">
                </form>
            </body>
            </html>
        """)

    def do_POST(self):
        # Получаем данные формы
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')
        params = parse_qs(post_data)
        user = params.get('user', ['Гость'])[0]

        # Формируем HTML-ответ
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        html = f"""
            <html>
            <head><title>Reply Page</title></head>
            <body>
                <h1>Hello, <i>{user}</i>!</h1>
                <a href="/">Вернуться</a>
            </body>
            </html>
        """
        self.wfile.write(html.encode('utf-8'))

if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), SimpleHandler)
    print("Сервер запущен: http://localhost:8000")
    server.serve_forever()



'ВТОРОЙ ВАРИАНТ'
#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import html  # Для безопасного вывода пользовательского ввода

class SimpleHandler(BaseHTTPRequestHandler):
    def _render_template(self, content):
        """Шаблон базовой HTML-страницы"""
        return f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Reply Page</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            padding: 40px;
        }}
        .container {{
            background: white;
            padding: 20px 30px;
            border-radius: 10px;
            max-width: 400px;
            margin: auto;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }}
        h1 {{ color: #333; }}
        input[type="text"] {{
            width: 100%;
            padding: 8px;
            margin: 10px 0;
            border-radius: 6px;
            border: 1px solid #ccc;
        }}
        input[type="submit"] {{
            padding: 8px 16px;
            border: none;
            background-color: #4CAF50;
            color: white;
            border-radius: 6px;
            cursor: pointer;
        }}
        input[type="submit"]:hover {{
            background-color: #45a049;
        }}
    </style>
</head>
<body>
    <div class="container">
        {content}
    </div>
</body>
</html>"""

    def do_GET(self):
        """Отображает форму"""
        html_form = """
            <h1>Введите своё имя</h1>
            <form method="POST">
                <input type="text" name="user" placeholder="Ваше имя">
                <input type="submit" value="Отправить">
            </form>
        """
        page = self._render_template(html_form)
        self._send_html(page)

    def do_POST(self):
        """Обрабатывает данные формы"""
        length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(length).decode("utf-8")
        params = parse_qs(post_data)
        user = html.escape(params.get("user", ["Гость"])[0])  # защита от XSS

        html_reply = f"""
            <h1>Привет, <i>{user}</i>!</h1>
            <a href="/">Вернуться назад</a>
        """
        page = self._render_template(html_reply)
        self._send_html(page)

    def _send_html(self, content):
        """Отправляет HTML-ответ"""
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(content.encode("utf-8"))

if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), SimpleHandler)
    print("✅ Сервер запущен: http://localhost:8000")
    print("Нажмите Ctrl+C для остановки.")
    server.serve_forever()


"Exercise 9 Сценарий для заполнения базы данных shelve объектами Python"
rec1 = {'name': {'first': 'Bob', 'last' : 'Smith'},
        'job': ['dev', 'mgr'],
        'age': 40.5}
rec2 = {'name': {'first':'Sue', 'last':'Jones'},
        'job': ['mgr'],
        'age': 35.0}

import shelve
db = shelve.open('dbfile')
db['bob'] = rec1
db['sue'] = rec2
db.close ()



"Exercise 10 Сценарий для вывода и заполнения базы данных shelve"
import shelve
db = shelve.open('dbfile')
for key in db:
    print(key, '=>', db[key])
bob = db [' bob']
bob['age'] += 1
db['bob'] = bob
db.close()


"Exercise 11 Сценарий для заполнения и запрашивания базы данных MySql"
from MySQLdb import Connect
conn = Connect(host='localhost', user='root', passwd='root1234+ROOT')
curs = conn.cursor()
try:
    curs.execute('drop database testpeopledb')
except:
    pass                                                        # He существует
curs.execute('create database testpeopledb')
curs.execute('use testpeopledb')
curs.execute('create table people (name char(30), job char(10), pay int(4))')
curs.execute('insert people values (%s, %s, %s)', ('Bob', 'dev', 50000))
curs.execute('insert people values (%s, %s, %s) ' , ('Sue', 'dev', 60000))
curs.execute('insert people values (%s, %s, %s)', ('Ann', 'mgr', 40000))
curs.execute('insert people values (%s, %s, %s)', ('Bax', 'mgr', 50000))
curs.execute('insert people values (%s, %s, %s)', ('Nas', 'mgr', 70000))
curs.execute('insert people values (%s, %s, %s)', ('Vik', 'mgr', 80000))

curs.execute('select * from people')
for row in curs. fetchall ():
    print(row)
curs.execute('select * from people where name = %s', ('Bob',))
print(curs.description)
colnames = [desc[0] for desc in curs.description]
while True:
    print('-' * 30)
    row = curs.fetchone()
    if not row: break
    for (name, value) in zip(colnames, row):
        print('%s => %s' % (name, value))
conn.commit()                                                     # Сохранить


"Exercise 12 Извлечение и открытие файла по протоколу FTP"
import webbrowser, sys
from ftplib import FTP
from getpass import getpass

nonpassive = False  # использовать активный режим FTP?

filename = input('File? ')
dirname = input('Dir? ') or '.'
sitename = input('Site? ')
user = input('User? ')  # Enter — для анонимного входа

if not user:
    userinfo = ()
else:
    userinfo = (user, getpass('Pswd? '))

print('Connecting...')
connection = FTP(sitename)
connection.login(*userinfo)
connection.cwd(dirname)

if nonpassive:
    connection.set_pasv(False)

print('Downloading...')
with open(filename, 'wb') as localfile:
    connection.retrbinary('RETR ' + filename, localfile.write, 1024)

connection.quit()
print('Playing...')
webbrowser.open(filename)



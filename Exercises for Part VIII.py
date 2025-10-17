"Файл patternparse.py"
import re
text = open('mybooks.xml').read()
found = re.findall('<title>(.*)</title>', text)
for title in found: print(title)


"Файл domparse.py"
from xml.dom.minidom import parse, Node
xmltree = parse('mybooks.xml')
for node1 in xmltree.getElementsByTagName('title'):
    for node2 in node1.childNodes:
        if node2.nodeType == Node.TEXT_NODE:
            print(node2.data)

"Файл saxparse.py"
import xml.sax.handler
class BookHandler(xml.sax.handler.ContentHandler):
    def __init__ (self) :
        self.inTitle = False
    def startElement(self, name, attributes):
        if name == ' title':
            self.inTitle = True
    def characters(self, data):
        if self.inTitle:
            print(data)
    def endElement(self, name):
        if name == 'title' :
            self.inTitle = False
import xml.sax
parser = xml.sax.make_parser()
handler = BookHandler()
parser.setContentHandler(handler)
parser.parse('mybooks.xml')

"Файл etreeparse.py"
from xml.etree.ElementTree import parse
tree = parse('mybooks.xml')
for E in tree.findall('title'):
    print(E.text)


import sys
f = open('py33-windows-launcher.html', encoding='utf8')
t = f.read()
for (i, c) in enumerate (t) :
    try:
        x = c.encode(encoding= 'ascii')
    except:
        print(i, sys.exc_infо()[0])

class Person:
    def __init__ (self, name):
        self._name = name
    def getName(self):
        print('fetch...')
        return self._name
    def setName(self, value):
        print('change...')
        self._name = value
    def delName(self) :
        print('remove...')
        del self._name
    name = property(getName, setName, delName, "name property docs")

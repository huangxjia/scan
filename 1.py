__author__ = 'Administrator'

from docx import *
from os import listdir
from os.path import isfile, join

def skip(document):
    d = opendocx(document)
    s = search(d,"620")
    if s == True:
        print str(f)

mypath = os.getcwd()

files = [f for f in listdir(mypath) if isfile(join(mypath,f))]

for f in files:
    if ('docx' in f):
        skip(f)


"""
import zipfile
z = zipfile.ZipFile("1.docx")
print z.read("word/document.xml")

"""
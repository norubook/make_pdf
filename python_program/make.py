import os
import tkinter as tk
from tkinter import filedialog

file = filedialog.askopenfilename(filetypes=[("","*")])
out_path = os.path.abspath(os.path.join(file, os.pardir))+'/'

fr = open(file,'r', encoding='UTF-8')
fr_txt= fr.read()
fr.close()
a=0
b="title"
c="main"
output='''
<!DOCUTYPE html>
<html>
<head>
<div id="title">
{}
</div>
<style>
</style>
</head>
<body>
<h1>
<section class="main"><p>{}</p>
</section>
</h1>
</body>
</html>
'''.format(b,fr_txt)
while 1:
 try:
  if a==0:
   f = open('{}test.html'.format(out_path), 'x', encoding='UTF-8')
   break
  else:
   f = open('{}test_{}.html'.format(out_path,str(a)), 'x', encoding='UTF-8')
   break

 except:
  a+=1

f.write(output)
f.close()
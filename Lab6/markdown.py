"""
 Markdown.py
 0. just print whatever is passed in to stdin
 0. if filename passed in as a command line parameter, 
    then print file instead of stdin
 1. wrap input in paragraph tags
 2. convert single asterisk or underscore pairs to em tags
 3. convert double asterisk or underscore pairs to strong tags

"""

import fileinput
import re

def convertStrong(line):
  line = re.sub(r'\*\*(.*)\*\*', r'<strong>\1</strong>', line)
  line = re.sub(r'__(.*)__', r'<strong>\1</strong>', line)
  return line

def convertEm(line):
  line = re.sub(r'\*(.*)\*', r'<em>\1</em>', line)
  line = re.sub(r'_(.*)_', r'<em>\1</em>', line)
  return line

def convertHeader(line):
  s = re.search('(#+)',line)
  if s:
    n = len(s.group(1))
    line = re.sub(r'(#+)(.*)','<h'+str(n)+r'>\g<2></h'+str(n)+'>',line)
  return line


def convertBlockquote(lines):
  quotes = False
  for i in range(len(lines)):
    if re.search('^\>',lines[i]):
      if not quotes:
        lines[i] = re.sub(r'^\>(.*)', r'<blockquote>\1', lines[i])
        quotes = True
      else:
        lines[i] = re.sub(r'^\>(.*)', r'\1', lines[i])
      
    elif quotes:
      lines[i-1]+='</blockquote>'
      quotes = False
    lines[i] = convertStrong(lines[i])
    lines[i] = convertEm(lines[i])
    lines[i] = convertHeader(lines[i])
    if not re.search('<h',lines[i]):
      if re.search('^<blockquote>',lines[i]):
        lines[i] = re.sub(r'^<blockquote>(.*)','<blockquote><p>\g<1></p>',lines[i])
      else:
        lines[i] = '<p>'+lines[i]+'</p>'
    if quotes and i == len(lines)-1:
      lines[i]+='</blockquote>'        

lines = []
for line in fileinput.input():
  lines.append(line.rstrip())  

convertBlockquote(lines)

for line in lines:
  print line

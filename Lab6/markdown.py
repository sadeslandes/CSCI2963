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


def convertBlockquote(line, in_blockquote):
  s=re.search('\>',line)
  if s:
    if not in_blockquote:
      line = re.sub(r'\>(.*)', r'<blockquote>\1', line)
      in_blockquote = True
    else:
      line = re.sub(r'\>(.*)', r'', line)
  elif in_blockquote:
    in_blockquote = False
    line = '</blockquote>'+line
  return (line,in_blockquote) 

in_blockquote = False
for line in fileinput.input():
  line = line.rstrip() 
  res = convertBlockquote(line,in_blockquote)
  line = res[0]
  line = convertStrong(line)
  line = convertEm(line)
  line = convertHeader(line)
  in_blockquote = res[1]
  print '<p>' + line + '</p>',

import re
import sys

filename = sys.argv[1]

def replaceChapterDivisions(text): 
    pattern = r'(?ms)<A NAME="chap(\d\d)"></A>\n<H3.*?>\n(.*?)\n</H3>'
    replacement = r'</div><div type="chapter" n="\1"><head>\2</head>'
    return re.sub(pattern, replacement, text)

text = open(filename).read()
with open(filename) as f:
    text = f.read()
    f.close()

with open(filename, 'w') as f:
    replaced = replaceChapterDivisions(text)
    f.write(replaced)
    f.close()

import re
import sys

filename = sys.argv[1]

print("Processing file: " + filename)

text = open(filename).read()

pattern = r'(?ms)(\s)(")(.*?)(")(\s|[:;])'
replacement = r'\1<said>\3</said>\5'
print(re.sub(pattern, replacement, text))

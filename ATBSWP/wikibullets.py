#! python3
#Adds wiki bullets to start of each line on clipboard

import pyperclip
text = pyperclip.paste()
new_text = ''
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)


#! python3

import pyperclip
text=pyperclip.paste()
lines=text.splitlines()

for i in range(len(lines)):
    lines[i]='* '+lines[i]
text='\n'.join(lines)

print(text)



pyperclip.copy(text)

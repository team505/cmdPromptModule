
from cmdPromptModule import main

newCmd('hi')

while True:
	txt = input('/n>>>')
	cmd(txt, 'hi', 'hello')
	help(txt)
	

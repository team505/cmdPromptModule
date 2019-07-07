
global cmd
cmd = []

def cmd(txt, trigger, answer):
	if txt == trigger:
		print(answer)
		return True
	else:
		return False
		
def on(function, output, noutput):
	if function:
		print(output)
		return True
	else:
		print(noutput)
		return False
		

def help(txt):
	if txt == 'help':
		print(cmd)

def newCmd(cmd):
	cmd.append(cmd)

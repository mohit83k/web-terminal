import subprocess

def run(cmd):
	'''
	Run the command, wait for it to execute and return the output.
	'''
	done = subprocess.run("cmd /c "+cmd,text=True , stdout=subprocess.PIPE , stderr=subprocess.PIPE)
	return done.stdout , done.stderr


if __name__ == "__main__":
	print(run('dir'))


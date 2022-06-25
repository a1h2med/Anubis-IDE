import subprocess
import os

def __execute(cmd): 
	process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	output, error = process.communicate()
	return output, error

def __createAnubisFolder():
	if not os.path.exists(".Anubis"):
		os.mkdir(path=".Anubis")

def __writeSourceCodeToTempFile(sourceCode:str,tempPath:str):
	f = open(tempPath+"temp.py", "w")
	# changing the working directory to the default one not that of temp file
	f.write("import sys; sys.path.insert(0, sys.path[0]+'/..')")
	f.write(sourceCode)
	f.close()

def runPythonCode(sourceCode:str):
	__createAnubisFolder()
	__writeSourceCodeToTempFile(sourceCode,".Anubis/")
	cmd = "python3 .Anubis/temp.py"
	output, error =__execute(cmd)
	return output.decode(), error.decode()
import os
import subprocess

os.system("ls")
subprocess.run(["ls"])
subprocess.run(["ls", "-l"])
subprocess.run(["ls", "-l","README.md"])


#Exercise 5: Retrieving system information
command = "uname"
commanArgument = "-a"
print(f'Gathering system information with command: {command} {commanArgument}')
subprocess.run([command, commanArgument])

##Exercise 6: Retrieving information about disk space
command = "ps"
commandArgument = "-X"
print(f'Gathering activee process information with command: {command} {commanArgument}')
subprocess.run([command, commandArgument])

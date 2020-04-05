import os
import time

print(os.path.abspath("main.py"))

print(os.path.normpath("Workspace/main.py"))

print(os.path.relpath("Workspace/main.py"))

print(os.path.dirname("Workspace/main.py"))

print(os.path.basename("Workspace/main.py"))

print(os.path.join("Workspace","main.py"))

print(os.path.exists("main.py"))

print(os.path.isfile("/Users/lumin/Documents/GitHub.com/Python.Programming/程序设计/Workspace/main.py"))

print(os.path.isdir("/Users/lumin/Documents/GitHub.com/Python.Programming/程序设计/Workspace/"))

print(os.path.getatime("main.py"))
print(os.path.getmtime("main.py"))
print(time.ctime(os.path.getctime("main.py")))

print(os.path.getsize("main.py"))

os.system("/Applications/Calculator.app/Contents/MacOS/Calculator")

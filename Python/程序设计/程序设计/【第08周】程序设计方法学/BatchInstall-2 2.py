#BatchInstall.py
import os
libs = {"TKV", "numpy", "traits", "mayavi", "pyqt5"}
try:
    for lib in libs:
        os.system("pip3 install "+lib)
    print("Successful")        
except:
    print("Failed Somehow")

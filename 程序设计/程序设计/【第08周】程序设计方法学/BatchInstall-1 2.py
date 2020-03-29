#BatchInstall.py
import os
libs = {"matplotlib","pillow","sklearn","requests",\
        "jieba","beautifulsoup4","wheel","networkx","sympy",\
        "pyinstaller","django","flask","werobot","wordcloud",\
        "pandas","pyopengl","pypdf2","docopt","pygame"}
try:
    for lib in libs:
        os.system("pip3 install "+lib)
    print("Successful")        
except:
    print("Failed Somehow")

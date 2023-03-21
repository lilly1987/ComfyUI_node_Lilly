from .Colors import cprint, Colors as Colors
import os, sys
py_name=os.path.basename(__file__)
cprint(py_name, Colors.BLUE)

absFilePath = os.path.abspath(__file__)
cprint("abspath   : " + absFilePath , Colors.CYAN)

realFilePath = os.path.realpath(__file__)
cprint("realpath  : " + realFilePath , Colors.CYAN)

normpath=os.path.normpath(__file__)
cprint("normpath  : " + normpath , Colors.CYAN)

subfolder = os.path.dirname(normpath)
cprint("subfolder : " + subfolder , Colors.CYAN)

filename = os.path.basename(normpath)
cprint("filename  : " + filename , Colors.CYAN)
        
mainFile = os.path.abspath(sys.modules['__main__'].__file__)
cprint("mainFile  : " + mainFile , Colors.CYAN)

mainfolder = os.path.dirname(mainFile)
cprint("mainfolder : " + mainfolder , Colors.CYAN)


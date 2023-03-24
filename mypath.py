import sys
import json
import ast
import os
if __name__ == os.path.splitext(os.path.basename(__file__))[0] :
    from ConsoleColor import print, console
else:
    from .ConsoleColor import print, console

"""
import psutil
for proc in psutil.process_iter():
  ps_name = proc.name()
  if ps_name == 'python3':
    cmdline = proc.cmdline()
    print(cmdline)
"""

"""
print()
for key, value in os.environ.items():
    print('{}: {}'.format(key, value))
print()
"""

py_name=os.path.basename(__file__)
print("os.path.basename(__file__) : ",py_name, style="bold CYAN")

absFilePath = os.path.abspath(__file__)
print("os.path.abspath(__file__)  : " , absFilePath , style="bold CYAN")

realFilePath = os.path.realpath(__file__)
print("os.path.abspath(__file__)  : " + realFilePath , style="bold CYAN")

normpath=os.path.normpath(__file__)
print("os.path.normpath(__file__) : " + normpath , style="bold CYAN")

subfolder = os.path.dirname(normpath)
print("os.path.dirname(normpath) : " + subfolder , style="bold CYAN")

filename = os.path.basename(normpath)
print("os.path.basename(normpath) : " + filename , style="bold CYAN")

mainFile = os.path.abspath(sys.modules['__main__'].__file__)
print("os.path.abspath(sys.modules\['__main__'].__file__) : " + mainFile ,style="bold CYAN")
mainfolder = os.path.dirname(mainFile)
print("os.path.dirname(mainFile) : " + mainfolder , style="bold CYAN")

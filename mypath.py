import sys
import json
import os
if __name__ == os.path.splitext(os.path.basename(__file__))[0] :
    from ConsoleColor import print, console
else:
    from .ConsoleColor import print, console
#print(__file__)
#print(os.path.basename(__file__))


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

def jsondic(full,dic,update=False):
    
    path=os.path.split(full)[0]
    if not os.path.exists(path):
        os.makedirs(path)
    #with open(f"./RandomLoop/chars-{time.strftime('_%Y%m%d_%H%M%S')}.json", 'w', encoding='utf-8') as file:
    if os.path.exists(full):
        with open(full, 'r', encoding='utf-8') as file:
            tmp=json.load(file)
            if update:
                dic.update(tmp)
            else:
                dic=(tmp)
    else:
        with open(full, 'w', encoding='utf-8') as file:
            json.dump(dic, file, sort_keys=False, indent=4)
            
    return path
        
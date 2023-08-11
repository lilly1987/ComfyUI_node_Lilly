import sys
import json
import ast
import os, glob
import random
from folder_paths import *
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

def check_name(kind,name,supported_extensions):
    for ext in supported_extensions:
        if name.lower().endswith(ext):
            path = folder_paths.get_full_path(kind, name)
            if path is not None:
                return path
        
    for ext in supported_extensions:
        path = folder_paths.get_full_path(kind, name+ext)
        if path is not None:
            return path

def check_name_ckpt(name):
    return check_name("checkpoints",name,supported_ckpt_extensions)
    
def check_name_pt(kind,name):
    return check_name(kind,name,supported_pt_extensions)
    
def name_split_choice(name):
    return random.choice(name.split('|'))
    
#----------------------

def filenameget(v_path):
    t_path=os.path.join(os.path.dirname(__file__),v_path)
    print(t_path)
    fullpaths=glob.glob(t_path, recursive=True)
    print(fullpaths)
    fullpath=random.choice(fullpaths)
    name=os.path.basename(fullpath)
    #r_path=[os.path.basename(fullpath) for fullpath in fullpaths]
    return (name,fullpath)

# "test","vae",["pt","safetensors"]
def getFullPath(p,k,el=["safetensors","ckpt","pt"]):
    if os.path.isabs(p):
        path=p
    else:
        path=os.path.join(models_dir,k,"**",p)
    #print(f"path : ", path)
    t=False
    for e in el:
        if p.endswith('.'+e):
            t=True
            break
    if t:
        files=glob.glob(path, recursive=True)
    else:
        for e in el:
            t=path+"."+e
            #print(f"t : ", t)
            files=glob.glob(t, recursive=True)
            if len(files):
                break
    result=None
    #print(f"files : ", files)
    if len(files):
        result=random.choice(files)
        print(f"result : ", result)
    else:
        print("[red]No file in path[/red] : ", path)
    return result
import sys
import os
if __name__ == os.path.splitext(os.path.basename(__file__))[0] :
    from ConsoleColor import print, console
else:
    from .ConsoleColor import print, console
#print(__file__)
#print(os.path.basename(__file__))

#print(f"sys.modules : {sys.modules}")

#filePath = __file__
#print("This script file path is ", filePath)
#
#absFilePath = os.path.abspath(__file__)
#print("This script absolute path is ", absFilePath)
#
#realFilePath = os.path.realpath(__file__)
#print("This script real path is ", realFilePath)
#
#path, filename = os.path.split(absFilePath)
#print("Script file path is {}, filename is {}".format(path, filename))

wd = os.getcwd()
#print("working directory : ", wd)

nm=os.path.abspath(__name__)
#print("abspath __name__ : ", nm)

md=nm.replace(wd+"\\","")
#print("import name", md)
""" 
"""
#if md in sys.modules:
#    print(f"{md!r} already in sys.modules")
#else:
#    print(f"{md!r} not in sys.modules")
        
if not md.startswith("custom_nodes."):

    import importlib
    #from custom_nodes.ComfyUI_node_Lilly import eval(f"{name}")

    NODE_CLASS_MAPPINGS = {
    }

    def add(name):
        #print(f"Load : {name}")
        try:        
            pkg = importlib.import_module(f"{md}.{name}")
            NODE_CLASS_MAPPINGS[name]=eval(f"pkg.{name}")
            print(f"Load ok   : {name}", style="bold green")
        except Exception:
            console.print_exception()
    
    console.rule(f" init start ", style="bold green")
    
    add("CheckpointLoaderRandom")
    add("CheckpointLoaderSimpleText")
    add("CLIPTextEncodeWildcards")
    add("LoraLoaderText")
    add("LoraLoaderTextRandom")
    add("Random_Sampler")
    add("VAELoaderDecode")
    add("SimpleSampler")
    add("SaveImageSimple")
    #add("test")
    
    console.rule(" finit end ", style="bold green")
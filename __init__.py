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

    def add(name,clist=None):
        #print(f"Load : {name}")
        try:        
            pkg = importlib.import_module(f"{md}.{name}")
            if clist is None:
                NODE_CLASS_MAPPINGS[name]=eval(f"pkg.{name}")
            elif type(clist) is str:
                NODE_CLASS_MAPPINGS[clist]=eval(f"pkg.{clist}")
            elif type(clist) is list:
                for c in clist:
                    NODE_CLASS_MAPPINGS[c]=eval(f"pkg.{c}")
            print(f"Load ok   : {name}", style="bold green")
        except Exception:
            console.print_exception()
    
    console.rule(f" init start ", style="bold green")
    
    add("CheckpointLoaderRandom")
    add("CheckpointLoaderSimpleText")
    add("CLIPTextEncodeWildcards",["CLIPTextEncodeWildcards","CLIPTextEncodeWildcards2","CLIPTextEncodeWildcards3"])
    add("LoraLoaderText")
    add("LoraLoaderTextRandom")
    add("Random_Sampler")
    add("VAELoaderDecode")
    add("SimpleSampler",["SimpleSampler","SimpleSamplerVAE"])
    add("SaveImageSimple")
    #add("test")
    
    console.rule(" init end ", style="bold green")
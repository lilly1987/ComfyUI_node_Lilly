import sys
import os


#print(f"__name__ : {__name__}")
#print(f"__file__ : {__file__}")
#print(f"os.path.basename(__file__) : {os.path.basename(__file__)}")
#print(f"os.path.splitext(os.path.basename(__file__))[0] : {os.path.splitext(os.path.basename(__file__))[0]}")
#print(f"os.path.basename(__file__) : {os.path.basename('/ComfyUI_windows_portable/ComfyUI/custom_nodes/ComfyUI_node_Lilly/__init__.py')}")
#print(f"os.path.splitext(os.path.basename(__file__))[0] : {os.path.splitext(os.path.basename('/ComfyUI_windows_portable/ComfyUI/custom_nodes/ComfyUI_node_Lilly/__init__.py'))[0]}")

#wd = os.getcwd()
#print("working directory : ", wd)

#if __name__ == os.path.splitext(os.path.basename(__file__))[0] or __name__ =='__main__':    
    #from ConsoleColor import print, console
    #md="custom_nodes.ComfyUI_node_Lilly."
#else:
    #from .ConsoleColor import print, console
    #md="custom_nodes.ComfyUI_node_Lilly."
md="custom_nodes.ComfyUI_node_Lilly."
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


#
#nm=os.path.abspath(__name__)
#nm=os.path.abspath(__name__)
#print("abspath __name__ : ", nm)
#print("abspath __name__ : ", nm)
#
#md=nm.replace(wd+"\\","")
#print("import name", md)
""" 
"""
#if md in sys.modules:
#    print(f"{md!r} already in sys.modules")
#else:
#    print(f"{md!r} not in sys.modules")

#import importlib
#import ComfyUI_node_Lilly
#from custom_nodes.ComfyUI_node_Lilly import eval(f"{name}")
#print(dir(ComfyUI_node_Lilly))
#print(dir(ComfyUI_node_Lilly.ComfyUI_node_Lilly))

#print(__name__ == md)
#print(__name__ != md)
#print(__name__ == "ComfyUI_node_Lilly")
#print(__name__ != "ComfyUI_node_Lilly")
if __name__ == "ComfyUI_node_Lilly" :
    NODE_CLASS_MAPPINGS = {
    }

    def add(name,clist=None):
        #print(f"Load : {name}")
        try:        
            #pkg = importlib.import_module(f"{md}{name}")
            #eval(f"{md}{name}")
            exec(f"import {md}{name}")
            if clist is None:
                NODE_CLASS_MAPPINGS[name]=eval(f"{md}{name}.{name}")
            elif type(clist) is str:
                NODE_CLASS_MAPPINGS[clist]=eval(f"{md}{name}.{clist}")
            elif type(clist) is list:
                for c in clist:
                    NODE_CLASS_MAPPINGS[c]=eval(f"{md}{name}.{c}")
            
            print(f"Load ok   : {name}")
        except Exception as e:
            print(f"An exception occurred:", e)
            #console.print_exception()

    #console.rule(f" init start ", style="bold green")
    #print(f" init start ")
    print(f"### Loading: ComfyUI-node-Lilly")

    add("CheckpointLoaderRandom")
    add("CheckpointLoaderSimpleText")
    add("CLIPTextEncodeWildcards",["CLIPTextEncodeWildcards","CLIPTextEncodeWildcards2","CLIPTextEncodeWildcards3"])
    add("LoraLoaderText")
    add("LoraLoaderTextRandom")
    add("Random_Sampler")
    add("VAELoaderDecode")
    add("VAELoaderText")
    add("SimpleSampler",["SimpleSampler","SimpleSamplerVAE"])
    add("SaveImageSimple")
    add("TextWildcards")
    #add("test")

    #console.rule(" init end ", style="bold green")
    #print(f" init end ")
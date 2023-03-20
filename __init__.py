print("ComfyUI_node_Lilly.__init__")

import importlib
#from custom_nodes.ComfyUI_node_Lilly import eval(f"{name}")

NODE_CLASS_MAPPINGS = {
}

def add(name):
    print(f"Load : {name}")
    try:        
        pkg = importlib.import_module(f"custom_nodes.ComfyUI_node_Lilly.{name}")
        NODE_CLASS_MAPPINGS[name]=eval(f"pkg.{name}")
        print(f"ok   : {name}")
    except Exception as e:         
        print(f"Exception : {e}")

add("CheckpointLoaderRandom")
add("CheckpointLoaderSimpleText")
add("CLIPTextEncodeWildcards")
add("LoraLoaderText")
add("LoraLoaderTextRandom")
add("Random_Sampler")
add("VAELoaderDecode")
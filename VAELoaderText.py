import folder_paths
import comfy.sd
import os
from folder_paths import *
if __name__ == os.path.splitext(os.path.basename(__file__))[0] :
    #from ConsoleColor import print, console, ccolor
    from mypath import *
else:
    #from .ConsoleColor import print, console, ccolor
    from .mypath import *
    
class VAELoaderText:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": { 
                "vae_name": ("STRING", {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": random.choice(folder_paths.get_filename_list("vae")) 
                }),
        }}
    RETURN_TYPES = ("VAE",)
    FUNCTION = "load_vae"

    CATEGORY = "loaders"

    #TODO: scale factor?
    def load_vae(self, vae_name):
        print(f"[{ccolor}]vae_name : [/{ccolor}]", vae_name)
        vae_path=getFullPath(vae_name,"vae")
        try:
            vae = comfy.sd.VAE(ckpt_path=vae_path)
            return (vae,)
        except Exception as e:
            console.print_exception()
            return 
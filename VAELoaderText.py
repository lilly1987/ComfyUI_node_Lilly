import folder_paths
import comfy.sd
import os
from folder_paths import *
if __name__ == os.path.splitext(os.path.basename(__file__))[0] :
    from ConsoleColor import print, console
    from mypath import *
else:
    from .ConsoleColor import print, console
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
        if os.path.isabs(vae_name):
            vae_path=vae_name
        else:
            if vae_name.endswith('.safetensors') or vae_name.endswith('.pt') :
                vae_path = folder_paths.get_full_path("vae", vae_name)
            if vae_path is None:
                print(f"{vae_name} is none")
                if vae_name.endswith(".safetensors") or vae_name.endswith(".pt"):
                    (name,fullpath)=filenameget(os.path.join(models_dir, "vae")+"/**/"+vae_name)
                else:
                    (name,fullpath)=filenameget(os.path.join(models_dir, "vae")+"/**/"+vae_name+"*.safetensors")
                if fullpath is None:
                    print(f"{vae_name} is none")
                    return 
                vae_path=fullpath
            
        vae = comfy.sd.VAE(ckpt_path=vae_path)
        return (vae,)
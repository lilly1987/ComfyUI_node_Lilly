import os
import comfy.sd
from nodes import *
from folder_paths import *
import random 
import os
if __name__ == os.path.splitext(os.path.basename(__file__))[0] :
    from ConsoleColor import print, console, ccolor
    from mypath import *
else:
    from .ConsoleColor import print, console, ccolor
    from .mypath import *
    
#print(__file__)
#print(os.path.basename(__file__))

class CheckpointLoaderSimpleText:
    @classmethod
    def INPUT_TYPES(s):
        t_checkpoints=folder_paths.get_filename_list("checkpoints")
        #print(f"checkpoints count : {len(t_checkpoints)}", Colors.BGREEN)
        return {
            "required": { 
                "ckpt_name": (
                    "STRING", {
                        "multiline": False, 
                        "default": random.choice(t_checkpoints)
                    }
                ),
             }
         }
    RETURN_TYPES = ("MODEL", "CLIP", "VAE")
    FUNCTION = "load_checkpoint"

    CATEGORY = "loaders"
    
    def load_checkpoint(self, ckpt_name, output_vae=True, output_clip=True):
        print(f"[{ccolor}]ckpt_name : [/{ccolor}]", ckpt_name)
        ckpt_path=getFullPath(ckpt_name,"checkpoints")
        try:
            out = comfy.sd.load_checkpoint_guess_config(ckpt_path, output_vae=True, output_clip=True, embedding_directory=folder_paths.get_folder_paths("embeddings"))
            return out
        except Exception as e:
            console.print_exception()
            return 
            
        
#NODE_CLASS_MAPPINGS = {
#    "CheckpointLoaderSimpleText": CheckpointLoaderSimpleText,
#}
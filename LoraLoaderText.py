import os
import comfy.sd
from nodes import *
import folder_paths

if __name__ == os.path.splitext(os.path.basename(__file__))[0] :
    from ConsoleColor import print, console, ccolor
    from mypath import *
else:
    from .ConsoleColor import print, console, ccolor
    from .mypath import *

class LoraLoaderText:
    def __init__(self):
        self.loaded_lora = None
        
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": { 
                "model": ("MODEL",),
                  "clip": ("CLIP", ),
                "lora_name": ("STRING", {
                    "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                    "default": (folder_paths.get_filename_list("loras"), )
                }),
                  #"lora_name": (folder_paths.get_filename_list("loras"), ),
                  "strength_model": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.01}),
                  "strength_clip": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.01}),
            }
        }
    RETURN_TYPES = ("MODEL", "CLIP")
    FUNCTION = "load_lora"

    CATEGORY = "loaders"

    def load_lora(self, model, clip, lora_name, strength_model, strength_clip):
        
        print(f"[{ccolor}]lora_name : [/{ccolor}]", lora_name)
        if strength_model == 0 and strength_clip == 0:
            print("[red]strength_model,strength_clip 0[/red] : ", lora_name)
            return (model, clip)
            
        if lora_name is None or lora_name =="" :
            print("[red]No lora_name[/red] : ", lora_name)
            return (model, clip)
            
        lora_path = folder_paths.get_full_path("loras", lora_name)
        if lora_path is None:
            #print("[red]No lora_path of lora_name [/red] : ", lora_name)
            lora_path=getFullPath(lora_name,"loras")
            if lora_path is None:
                print("[red]No lora_path of lora_name [/red] : ", lora_name)
                return (model, clip)
            
        lora = None
        if self.loaded_lora is not None:
            if self.loaded_lora[0] == lora_path:
                lora = self.loaded_lora[1]
            else:
                del self.loaded_lora

        if lora is None:
            lora = comfy.utils.load_torch_file(lora_path, safe_load=True)
            self.loaded_lora = (lora_path, lora)
        
        # =========================================

        try:
            model_lora, clip_lora = comfy.sd.load_lora_for_models(model, clip, lora, strength_model, strength_clip)
            return (model_lora, clip_lora)
        except Exception as e:
            console.print_exception()
            return (model, clip)

#NODE_CLASS_MAPPINGS = {
#    "LoraLoaderText": LoraLoaderText,
#}
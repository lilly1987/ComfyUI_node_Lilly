import os
import comfy.sd
from nodes import *
import folder_paths
import random
if __name__ == os.path.splitext(os.path.basename(__file__))[0] :
    from ConsoleColor import print, console
    from mypath import *
else:
    from .ConsoleColor import print, console
    from .mypath import *

class LoraLoaderTextRandom:
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
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                #"lora_name": (folder_paths.get_filename_list("loras"), ),
                "strength_model_min": ("FLOAT", {"default": 0.50, "min": 0.0, "max": 10.0, "step": 0.01}),
                "strength_model_max": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 10.0, "step": 0.01}),
                "strength_clip_min": ("FLOAT", {"default": 0.50, "min": 0.0, "max": 10.0, "step": 0.01}),
                "strength_clip_max": ("FLOAT", {"default": 1.50, "min": 0.0, "max": 10.0, "step": 0.01}),
            }
        }
    RETURN_TYPES = ("MODEL", "CLIP")
    FUNCTION = "load_lora"

    CATEGORY = "loaders"

    def load_lora(self, 
        model, 
        clip, 
        lora_name, 
        seed,
        strength_model_min, 
        strength_model_max,
        strength_clip_min,
        strength_clip_max
        ):
        
        strength_model=random.uniform(min(strength_model_min,strength_model_max),max(strength_model_min,strength_model_max)) 
        strength_clip=random.uniform(min(strength_clip_min,strength_clip_max),max(strength_clip_min,strength_clip_max)) 

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
            model_lora, clip_lora = comfy.sd.load_lora_for_models(model, clip, lora_path, strength_model, strength_clip)
            return (model_lora, clip_lora)
        except Exception as e:
            console.print_exception()
            return (model, clip)

#NODE_CLASS_MAPPINGS = {
#    "LoraLoaderTextRandom": LoraLoaderTextRandom,
#}
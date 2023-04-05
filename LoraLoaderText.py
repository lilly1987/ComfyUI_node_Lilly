import os
import comfy.sd
from nodes import *
import folder_paths

if __name__ == os.path.splitext(os.path.basename(__file__))[0] :
    from ConsoleColor import print, console
else:
    from .ConsoleColor import print, console

class LoraLoaderText:
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
        
        if lora_name is None or lora_name =="":
            print("[red]No lora_name[/red] : ", lora_name)
            return (strength_model, strength_clip)
        
        if lora_name.endswith('.safetensors') or lora_name.endswith('.ckpt') :
            lora_path = folder_paths.get_full_path("loras", lora_name)
            
        else:
            lora_path = folder_paths.get_full_path("loras", lora_name+'.safetensors')
            if lora_path is None:
                lora_path = folder_paths.get_full_path("loras", lora_name+'.ckpt')
                if lora_path is None:
                    print("[red]No lora_name[/red] : ", lora_name)
                    return (model, clip)
                #else:
                    #print("[green]lora_path : [/green]"+ lora_path)
            #else:
                #print("[green]lora_path : [/green]"+ lora_path)
        print("[green]lora_path : [/green]"+ lora_path)
                
        try:
            model_lora, clip_lora = comfy.sd.load_lora_for_models(model, clip, lora_path, strength_model, strength_clip)
            return (model_lora, clip_lora)
        except Exception as e:
            console.print_exception()
            return (model, clip)

#NODE_CLASS_MAPPINGS = {
#    "LoraLoaderText": LoraLoaderText,
#}
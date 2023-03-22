import os
import comfy.sd
from nodes import *
import folder_paths
import random
from .check_name import *

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

        lora_path =check_name_pt("loras",name_split_choice(lora_name))
        if lora_path is None:
            print(f"LoraLoaderTextRandom : {lora_name} is none")
            return (model, clip)
        print(f"LoraLoaderTextRandom : {lora_path} ")
        try:
            model_lora, clip_lora = comfy.sd.load_lora_for_models(model, clip, lora_path, strength_model, strength_clip)
            return (model_lora, clip_lora)
        except Exception as e:
            print(f"LoraLoaderTextRandom Exception : {e}" )
            err_msg = traceback.format_exc()
            print(err_msg)
            return (model, clip)

#NODE_CLASS_MAPPINGS = {
#    "LoraLoaderTextRandom": LoraLoaderTextRandom,
#}
import os
import comfy.sd
from nodes import *
import random
import folder_paths

cnt=0
ckpt_name=""
ckpt_path=""

class CheckpointLoaderRandom:
    models_dir = os.path.join(os.getcwd(),"ComfyUI", "models")
    ckpt_dir = os.path.join(models_dir, "checkpoints")
    cnt=0
    ckpt_name=""
    ckpt_path=""
    
    def __init__(self):
        print(f"CheckpointLoaderRandom __init__")
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": { 
            "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            "max": ("INT", {"default": 10, "min": 0, "max": 0xffffffffffffffff}),
            #"ckpt_name": (filter_files_extensions(recursive_search(s.ckpt_dir), supported_ckpt_extensions), ),
            }
        }
    RETURN_TYPES = ("MODEL", "CLIP", "VAE")
    FUNCTION = "load_checkpoint"

    CATEGORY = "loaders"

    def load_checkpoint(self, seed, max, output_vae=True, output_clip=True):
        global cnt, ckpt_name, ckpt_path
        print(f"cnt : { cnt}")
        if ckpt_name=="" or cnt>=max :
            cnt=0
            ckpt_names= folder_paths.get_filename_list("checkpoints")
            #print(f"ckpt_names : { ckpt_names}")
            ckpt_name=random.choice(ckpt_names)
            print(f"ckpt_name : { ckpt_name}")        
            ckpt_path = folder_paths.get_full_path("checkpoints",  ckpt_name)
        out = comfy.sd.load_checkpoint_guess_config(ckpt_path, output_vae=True, output_clip=True, embedding_directory=folder_paths.get_folder_paths("embeddings"))
        cnt+=1
        return out
        

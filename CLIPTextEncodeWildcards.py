import os, glob, sys
import random
import re
from .wildcards import *
#import wildcards

print("wildcards_ComfyUI")
#print(os.getcwd())

class CLIPTextEncodeWildcards:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"text": ("STRING", {"multiline": True}), "clip": ("CLIP", )}}
    RETURN_TYPES = ("CONDITIONING",)
    FUNCTION = "encode"

    CATEGORY = "conditioning"

    def encode(self, clip, text):
        r=run(text)
        print(f"encode : {r}")
        return ([[clip.encode(r), {}]], )

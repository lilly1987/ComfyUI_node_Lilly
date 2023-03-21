import os, glob, sys
import random
import re
from .wildcards import wildcards
#import wildcards

print("wildcards_ComfyUI")
#print(os.getcwd())
print(f"CLIPTextEncodeWildcards __name__ {__name__}")

class CLIPTextEncodeWildcards:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"text": ("STRING", {"multiline": True}), "clip": ("CLIP", )}}
    RETURN_TYPES = ("CONDITIONING",)
    FUNCTION = "encode"

    CATEGORY = "conditioning"

    def encode(self, clip, text):
        r=wildcards.run(text)
        print(f"encode : {r}")
        return ([[clip.encode(r), {}]], )

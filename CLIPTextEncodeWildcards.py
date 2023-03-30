import os, glob, sys
import random
import re
import os
if __name__ == os.path.splitext(os.path.basename(__file__))[0] or __name__ =='__main__':
    from ConsoleColor import print, console
    from wildcards import wildcards
else:
    from .ConsoleColor import print, console
    from .wildcards import wildcards
#print(__file__)
#print(os.path.basename(__file__))

#print("wildcards_ComfyUI")
#print(os.getcwd())
#Wprint(f"CLIPTextEncodeWildcards __name__ {__name__}")

class CLIPTextEncodeWildcards:
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "text": ("STRING", {"multiline": True}), "clip": ("CLIP", )
        }
        }
    RETURN_TYPES = ("CONDITIONING",)
    FUNCTION = "encode"

    CATEGORY = "conditioning"

    def encode(self, clip, text):
        print(f"[green]text : [/green]",text)
        r=wildcards.run(text)
        print(f"[green]result : [/green]",r)
        return ([[clip.encode(r), {}]], )

class CLIPTextEncodeWildcards2:
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "text": ("STRING", {"multiline": True}), "clip": ("CLIP", ),
            "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            
        }
        }
    RETURN_TYPES = ("CONDITIONING",)
    FUNCTION = "encode"

    CATEGORY = "conditioning"

    def encode(self, seed, clip, text):
        random.seed(seed)
        print(f"[green]text : [/green]",text)
        r=wildcards.run(text)
        print(f"[green]result : [/green]",r)
        return ([[clip.encode(r), {}]], )



class CLIPTextEncodeWildcards3:
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "clip": ("CLIP", ),
            "positive": ("STRING", {"multiline": True}),
            "negative": ("STRING", {"multiline": True}),
            "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            
        }
        }
    RETURN_TYPES = ("CONDITIONING","CONDITIONING")
    FUNCTION = "encode"

    CATEGORY = "conditioning"

    def encode(self, seed, clip, positive, negative):
        random.seed(seed)
        print(f"[green]positive : [/green]",positive)
        positive=wildcards.run(positive)
        print(f"[green]result : [/green]",positive)
        print(f"[green]negative : [/green]",negative)
        negative=wildcards.run(negative)
        print(f"[green]result : [/green]",negative)
        return ([[clip.encode(positive), {}]], [[clip.encode(negative), {}]], )



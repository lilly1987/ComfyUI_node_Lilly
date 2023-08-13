import os, glob, sys
import random
import re
import os
if __name__ == os.path.splitext(os.path.basename(__file__))[0] or __name__ =='__main__':
    #from ConsoleColor import print, console
    from wildcards import wildcards
else:
    #from .ConsoleColor import print, console
    from .wildcards import wildcards


class TextWildcards:
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "text": ("STRING", {"multiline": True}),
            "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
            
        }
        }
    RETURN_TYPES = ("STRING","ASCII")
    FUNCTION = "encode"

    CATEGORY = "utils"

    def encode(self, seed, text):
        random.seed(seed)
        print(f"[green]text : [/green]",text)
        r=wildcards.run(text)
        print(f"[green]result : [/green]",r)
        return (r, r)
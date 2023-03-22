from PIL import Image
from PIL.PngImagePlugin import PngInfo
import numpy as np
import json

import time

import os
if __name__ == os.path.splitext(os.path.basename(__file__))[0] :
    from ConsoleColor import print, console
    from mypath import *
else:
    from .ConsoleColor import print, console
    from .mypath import *
print(__file__)
print(os.path.basename(__file__))


class SaveImageSimple:
    def __init__(self):
        self.type = "output"
        
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "images": ("IMAGE", ),
                "filename_prefix": ("STRING", {"default": ""})
            },
            "hidden": {
                "prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO"
            },
        }
    RETURN_TYPES = ()
    FUNCTION = "save_images"

    OUTPUT_NODE = True

    CATEGORY = "image"

    def save_images(self, images, filename_prefix="", prompt=None, extra_pnginfo=None):

        outputdir=os.path.join(mainfolder, "output")
        #print("outputdir : " + outputdir , Colors.CYAN)

        #print("len(images) : " + str(len(images)) , Colors.CYAN)
        filename_prefix+=time.strftime('_%Y%m%d_%H%M%S')
        results = list()
        cnt=1
        for image in images :
            i = 255. * image.cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
            metadata = PngInfo()
            if prompt is not None:
                metadata.add_text("prompt", json.dumps(prompt))
            if extra_pnginfo is not None:
                #print("extra_pnginfo : " + json.dumps(extra_pnginfo) , Colors.CYAN)
                for x in extra_pnginfo:
                    metadata.add_text(x, json.dumps(extra_pnginfo[x]))
            if not os.path.exists(outputdir):
                print("makedirs  : " + outputdir , Colors.CYAN)
                os.makedirs(outputdir)            
            filename=filename_prefix+f"_{cnt:05}_.png"
            filename=os.path.join(outputdir, filename)
            img.save(filename, pnginfo=metadata, optimize=True)
            results.append({
                "filename": filename,
                "subfolder": subfolder,
                "type": self.type
            });
            cnt+=1
            
        return { "ui": { "images": results } }
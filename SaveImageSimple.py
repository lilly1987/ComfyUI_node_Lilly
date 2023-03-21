from PIL import Image
from PIL.PngImagePlugin import PngInfo
import numpy as np
import json

import time

from .Colors import cprint, Colors as Colors
import os, sys
py_name=os.path.basename(__file__)
cprint(py_name, Colors.BLUE)

from .mypath import *

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
        #cprint("outputdir : " + outputdir , Colors.CYAN)

        #cprint("len(images) : " + str(len(images)) , Colors.CYAN)
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
                #cprint("extra_pnginfo : " + json.dumps(extra_pnginfo) , Colors.CYAN)
                for x in extra_pnginfo:
                    metadata.add_text(x, json.dumps(extra_pnginfo[x]))
            if not os.path.exists(outputdir):
                cprint("makedirs  : " + outputdir , Colors.CYAN)
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
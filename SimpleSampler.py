import comfy.samplers
import comfy.sd
import comfy.utils

import comfy_extras.clip_vision

import model_management
import importlib

import folder_paths
import torch

import os
import sys
import json
import hashlib
import copy
import traceback

from PIL import Image
from PIL.PngImagePlugin import PngInfo
import numpy as np

print(f"SimpleSampler __name__ {__name__}")
print(f"SimpleSampler __file__ {os.path.splitext(os.path.basename(__file__))[0]}")

import os
if __name__ == os.path.splitext(os.path.basename(__file__))[0] :
    from ConsoleColor import print, console
else:
    from .ConsoleColor import print, console
print(__file__)
print(os.path.basename(__file__))

#----------------------------
# wildcards support check
wildcardsOn=False
try:
    from wildcards import *
    wildcardsOn=True
    #wildcards.card_path=os.path.dirname(__file__)+"\\..\\wildcards\\**\\*.txt"
    print(f"import wildcards succ", style="bold GREEN" )
except:
    print(f"import wildcards fail", style="bold RED")
    wildcardsOn=False
    err_msg = traceback.format_exc()
    print(err_msg)
    
#----------------------------
class SimpleSampler:
    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                    {
                    "model": ("MODEL",),
                    #"positive": ("CONDITIONING", ),
                    "positive": ("STRING", {"multiline": True}), "clip": ("CLIP", ),
                    #"negative": ("CONDITIONING", ),
                    "negative": ("STRING", {"multiline": True}), "clip": ("CLIP", ),
                    "width": ("INT", {"default": 512, "min": 64, "max": 4096, "step": 64}),
                    "height": ("INT", {"default": 512, "min": 64, "max": 4096, "step": 64}),
                    "batch_size": ("INT", {"default": 1, "min": 1, "max": 64}),
                    "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                    "steps": ("INT", {"default": 20, "min": 1, "max": 10000}),
                    "cfg": ("FLOAT", {"default": 8.0, "min": 0.0, "max": 100.0}),
                    "sampler_name": (comfy.samplers.KSampler.SAMPLERS, ),
                    "scheduler": (comfy.samplers.KSampler.SCHEDULERS, ),
                    "latent_image": ("LATENT", ),
                    "denoise": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01}),
                    }}

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "sample"

    CATEGORY = "sampling"
    
    def encode(self, clip, text):    
        if wildcardsOn:
            text=wildcards.run(text)
        return ([[clip.encode(text), {}]], )

    def generate(self, width, height, batch_size=1):
        latent = torch.zeros([batch_size, 4, height // 8, width // 8])
        return ({"samples":latent}, )

    def sample(self, 
        model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, 
        width, height, denoise=1.0, batch_size=1
        ):

        return common_ksampler(model, seed, steps, cfg, sampler_name, scheduler, self.encode(clip, positive), elf.encode(clip, negative), self.generate( width, height, batch_size=1), denoise=denoise)
        

import comfy.samplers
import comfy.sd
import comfy.utils

#import comfy_extras.clip_vision

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
from nodes import common_ksampler
from PIL.PngImagePlugin import PngInfo
import numpy as np

#print(f"SimpleSampler __name__ {__name__}")
#print(f"SimpleSampler __file__ {os.path.splitext(os.path.basename(__file__))[0]}")

import os


if __name__ == os.path.splitext(os.path.basename(__file__))[0] or __name__ =='__main__':
    from ConsoleColor import print, console
    from wildcards import wildcards
else:
    from .ConsoleColor import print, console
    from .wildcards import wildcards
#print(__file__)
#print(os.path.basename(__file__))

#----------------------------
wildcardsOn=True
# wildcards support check
#wildcardsOn=False
#try:
#    wildcardsOn=True
#    #wildcards.card_path=os.path.dirname(__file__)+"\\..\\wildcards\\**\\*.txt"
#    print(f"import wildcards succ", style="bold GREEN" )
#except:
#    print(f"import wildcards fail", style="bold RED")
#    wildcardsOn=False
#    err_msg = traceback.format_exc()
#    print(err_msg)
    
    
def encode(clip, text):    
    if wildcardsOn:
        text=wildcards.run(text)
    return [[clip.encode(text), {}]]
    
def generate(width, height, batch_size=1):
    latent = torch.zeros([batch_size, 4, height // 8, width // 8])
    return {"samples":latent}
    # RETURN_TYPES = ("LATENT",)
    
def decode(vae, samples):
    return vae.decode(samples["samples"])
    # RETURN_TYPES = ("IMAGE",)
    
def sample(
    model, seed, steps, cfg, sampler_name, scheduler, 
    clip,
    vae,
    positive, negative, 
    #latent_image, 
    width, height, denoise=1.0, batch_size=1
    ):

    samples=common_ksampler(
        model, seed, steps, cfg, sampler_name, scheduler, 
        #positive, 
        encode(clip, positive),
        #negative, 
        encode(clip, negative),
        #latent_image, 
        generate( width, height, batch_size=1), 
        denoise=denoise)[0]

    return (decode(vae,samples),)
    
def load_vae(vae_name):
    vae_path = folder_paths.get_full_path("vae", vae_name)
    vae = comfy.sd.VAE(ckpt_path=vae_path)
    return vae
#----------------------------
class SimpleSampler:
    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                    {
                    "model": ("MODEL",),
                    #"positive": ("CONDITIONING", ),
                    "clip": ("CLIP", ),
                    "vae": ("VAE", ),
                    "positive": ("STRING", {"multiline": True}), 
                    #"negative": ("CONDITIONING", ),
                    "negative": ("STRING", {"multiline": True}), 
                    "width": ("INT", {"default": 512, "min": 64, "max": 4096, "step": 64}),
                    "height": ("INT", {"default": 512, "min": 64, "max": 4096, "step": 64}),
                    "batch_size": ("INT", {"default": 1, "min": 1, "max": 64}),
                    "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                    "steps": ("INT", {"default": 20, "min": 1, "max": 10000}),
                    "cfg": ("FLOAT", {"default": 3.0, "min": 0.0, "max": 100.0}),
                    "sampler_name": (comfy.samplers.KSampler.SAMPLERS, ),
                    "scheduler": (comfy.samplers.KSampler.SCHEDULERS, ),
                    #"latent_image": ("LATENT", ),
                    "denoise": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01}),
                    }}
    RETURN_TYPES = ("IMAGE",)
    #RETURN_TYPES = ("LATENT",)
    FUNCTION = "simple"

    CATEGORY = "sampling"
    
    def simple(self, 
        model, seed, steps, cfg, sampler_name, scheduler, 
        clip,
        vae,
        positive, negative, 
        width, height, denoise=1.0, batch_size=1
        ):

        return sample(
            model, seed, steps, cfg, sampler_name, scheduler, 
            clip,
            vae,
            positive, negative, 
            width, height, denoise, batch_size
            )

#----------------------------
class SimpleSamplerVAE:
    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                    {
                    "model": ("MODEL",),
                    #"positive": ("CONDITIONING", ),
                    "clip": ("CLIP", ),
                    #"vae": ("VAE", ),
                    "vae_name": (folder_paths.get_filename_list("vae"), ),
                    "positive": ("STRING", {"multiline": True}), 
                    #"negative": ("CONDITIONING", ),
                    "negative": ("STRING", {"multiline": True}), 
                    "width": ("INT", {"default": 512, "min": 64, "max": 4096, "step": 64}),
                    "height": ("INT", {"default": 512, "min": 64, "max": 4096, "step": 64}),
                    "batch_size": ("INT", {"default": 1, "min": 1, "max": 64}),
                    "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                    "steps": ("INT", {"default": 20, "min": 1, "max": 10000}),
                    "cfg": ("FLOAT", {"default": 3.0, "min": 0.0, "max": 100.0}),
                    "sampler_name": (comfy.samplers.KSampler.SAMPLERS, ),
                    "scheduler": (comfy.samplers.KSampler.SCHEDULERS, ),
                    #"latent_image": ("LATENT", ),
                    "denoise": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01}),
                    }}
    RETURN_TYPES = ("IMAGE",)
    #RETURN_TYPES = ("LATENT",)
    FUNCTION = "simple"

    CATEGORY = "sampling"
    
    def simple(self, 
        model, seed, steps, cfg, sampler_name, scheduler, 
        clip,
        vae_name,
        positive, negative, 
        width, height, denoise=1.0, batch_size=1
        ):

        return sample(
            model, seed, steps, cfg, sampler_name, scheduler, 
            clip,
            load_vae(vae_name),
            positive, negative, 
            width, height, denoise, batch_size
            )


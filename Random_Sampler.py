import os
import nodes
import comfy.samplers
import random
from nodes import common_ksampler

#wd = os.getcwd()
#print("working directory is ", wd)
#
#filePath = __file__
#print("This script file path is ", filePath)
#
#absFilePath = os.path.abspath(__file__)
#print("This script absolute path is ", absFilePath)
#
#path, filename = os.path.split(absFilePath)
#print("Script file path is {}, filename is {}".format(path, filename))


class Random_Sampler:
    def __init__(self):
        print(f"Random_Sampler __init__")
        pass
        
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL",),
                "positive": ("CONDITIONING", ),
                "negative": ("CONDITIONING", ),
                "LATENT": ("LATENT", ),
                "sampler_name": (comfy.samplers.KSampler.SAMPLERS, ),
                "scheduler": (comfy.samplers.KSampler.SCHEDULERS, ),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                #"Random": (["enable", "disable"],),
                "steps_min": ("INT", {"default": 20, "min": 1,"max": 10000, "step": 1 }),
                "steps_max": ("INT", {"default": 30, "min": 1,"max": 10000, "step": 1 }),
                "cfg_min": ("FLOAT", {"default": 5.0, "min": 0.0, "max": 100.0, "step": 0.5}),
                "cfg_max": ("FLOAT", {"default": 9.0, "min": 0.0, "max": 100.0, "step": 0.5}),
                "denoise_min": ("FLOAT", {"default": 0.50, "min": 0.01, "max": 1.0, "step": 0.01}),
                "denoise_max": ("FLOAT", {"default": 1.00, "min": 0.01, "max": 1.0, "step": 0.01}),
            },
        }
        
    RETURN_TYPES = ("LATENT",)
    FUNCTION = "test"
    
    OUTPUT_NODE = False
    
    CATEGORY = "sampling"
    
    def test(self, 
        model, 
        positive, 
        negative, 
        LATENT, 
        sampler_name, 
        scheduler, 
        seed, 
        #Random, 
        steps_min, 
        steps_max, 
        cfg_min,
        cfg_max,
        denoise_min,
        denoise_max,
        ):
        print(f"""
    model : {model} ; 
    positive : {positive} ; 
    negative : {negative} ; 
    LATENT: {LATENT} ; 
    sampler_name : {sampler_name} ; 
    scheduler: {scheduler} ; 
    {seed} ; 
    
    {steps_min} ; 
    {steps_max} ; 
    {cfg_min} ; 
    {cfg_max} ; 
    {denoise_min} ; 
    {denoise_max} ; 
        """)
        #if Random == "enable":
        #    print(f"Random enable")
        #    return common_ksampler(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=denoise)
        return common_ksampler(
            model, 
            seed, 
            random.randint( min(steps_min,steps_max), max(steps_min,steps_max) ), 
            random.randint( int(cfg_min*2) , int(cfg_max*2) ) / 2 , 
            sampler_name, 
            scheduler, 
            positive, 
            negative, 
            LATENT, 
            denoise=random.uniform(min(denoise_min,denoise_max),max(denoise_min,denoise_max)) 
        )
        #return (LATENT,)
        
#NODE_CLASS_MAPPINGS = {
#    "Random_Sampler": Random_Sampler
#}
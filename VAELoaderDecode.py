import os
import comfy.sd
from nodes import *
import folder_paths


# VAEDecode
# VAELoader
# VAELoaderDecode

#wd = os.getcwd()
#print("working directory is ", wd)
#
#filePath = __file__
#print("This script file path is ", filePath)
#
#absFilePath = os.path.abspath(__file__)
#print("This script absolute path is ", absFilePath)
#
#realFilePath = os.path.realpath(__file__)
#print("This script real path is ", realFilePath)
#
#path, filename = os.path.split(absFilePath)
#print("Script file path is {}, filename is {}".format(path, filename))
        
class VAELoaderDecode:

    def __init__(self, device="cpu"):
        self.device = device

    #@classmethod
    #def INPUT_TYPES(s):
    #    return {"required": { "samples": ("LATENT", ), "vae": ("VAE", )}}
    #    
    #@classmethod
    #def INPUT_TYPES(s):
    #    return {"required": { "vae_name": (filter_files_extensions(recursive_search(s.vae_dir), supported_pt_extensions), )}}
        
    @classmethod
    def INPUT_TYPES(s):

        return {
            "required": { 
                "samples": ("LATENT", ),
                "vae_name": (folder_paths.get_filename_list("vae"), )
            }
        }
        
    RETURN_TYPES = ("IMAGE",)
    
    FUNCTION = "test"

    CATEGORY = "latent"

    #TODO: scale factor?
    #def load_vae(self, vae_name):
    #    vae_path = os.path.join(self.vae_dir, vae_name)
    #    vae = comfy.sd.VAE(ckpt_path=vae_path)
    #    return (vae,)
    #    
    #def decode(self, vae, samples):
    #    return (vae.decode(samples["samples"]), )        
        
    def test(self, vae_name, samples):

        t=folder_paths.get_filename_list("vae")
        print(f"VAELoaderDecode : {t}")
        vae_path = folder_paths.get_full_path("vae", vae_name)
        print(f"VAELoaderDecode : {vae_path}")
        vae = comfy.sd.VAE(ckpt_path=vae_path)
        return (vae.decode(samples["samples"]), )
        
#NODE_CLASS_MAPPINGS = {
#    "VAELoaderDecode": VAELoaderDecode,
#}
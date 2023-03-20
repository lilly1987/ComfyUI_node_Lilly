import os
from folder_paths import supported_ckpt_extensions,supported_pt_extensions
import folder_paths
import random

def check_name(kind,name,supported_extensions):
    for ext in supported_extensions:
        if name.lower().endswith(ext):
            path = folder_paths.get_full_path(kind, name)
            if path is not None:
                return path
        
    for ext in supported_extensions:
        path = folder_paths.get_full_path(kind, name+ext)
        if path is not None:
            return path

def check_name_ckpt(name):
    return check_name("checkpoints",name,supported_ckpt_extensions)
    
def check_name_pt(kind,name):
    return check_name(kind,name,supported_pt_extensions)
    
def name_split_choice(name):
    return random.choice(name.split('|'))
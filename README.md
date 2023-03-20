# ComfyUI-node-Lilly

## install
ComfyUI_windows_portable\ComfyUI\custom_nodes\ComfyUI_node_Lilly


## wildcards

### ex

- form
a{__b__|{c|}|{__d__|e|}|f|}g____ __my__
 
- to
aeg __quality_my__, __breasts__, { |__character_dress__|__dress_my__}, __shoulder__, {high heels,| } {choker,| } {<lora:__lora_lst__:__rora_num__>,| } NSFW, __NSFW_my__, { |__style_my__,}


### run sample

```
python wildcards.py
```

### python sample

```
import wildcards as w

# 가져올 파일 목록. get wildcards file
w.card_path=os.path.dirname(__file__)+"\\wildcards\\**\\*.txt"

# 실행 run
print(w.run("a{__b__|{c|}|{__d__|e|}|f|}g____ __my__"))
```

### 

```
wildcards.py # modul file
wildcards/*.txt # wildcards file
wildcards/**/*.txt # wildcards file
```

### txt file (UTF8)

```
# 주석
a,b
{b|c|__anotherfile__}
__anotherfile__
```
result
```
a,b
b
c
__anotherfile__
```

## for ComfyUI

![2023-03-20 02 13 50](https://user-images.githubusercontent.com/20321215/226194627-b560c9e1-5dfa-49d9-8503-939693a8b119.png)







## random_sampler_node.py

![2023-03-18 20 53 37](https://user-images.githubusercontent.com/20321215/226104447-eadd1d15-437f-4a41-b989-511390236d13.png)

## VAELoaderDecode.py

![2023-03-18 20 52 27](https://user-images.githubusercontent.com/20321215/226104441-a13f49c6-c5be-4c70-b93e-f4ad984e9ff1.png)

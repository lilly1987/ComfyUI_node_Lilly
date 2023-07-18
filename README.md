# ComfyUI-node-Lilly

## install

Go to ./custom_nodes and clone git repo:

```
cd ./custom_nodes
git clone https://github.com/kuriot/ComfyUI_node_Lilly.git
```
or https://github.com/lilly1987/ComfyUI_node_Lilly/archive/refs/heads/main.zip install this like

![2023-03-22 05 54 43](https://user-images.githubusercontent.com/20321215/226738610-c042a51c-8e72-45de-b714-385eaac383af.png)


## wildcards

### ex - wildcard

- form :  
a{__b__|{c|}|{__d__|e|}|f|}g____ __my__
 
- to :  
aeg __quality_my__, __breasts__, { |__character_dress__|__dress_my__}, __shoulder__, {high heels,| } {choker,| } {<lora:__lora_lst__:__rora_num__>,| } NSFW, __NSFW_my__, { |__style_my__,}

```
ex : {3$$a1|{b2|c3|}|d4|{-$$|f|g}|{-2$$h||i}|{1-$$j|k|}}/{$$l|m|}/{0$$n|}
{1|2|3} -> 1 or 2 or 3
{2$$a|b|c} -> a,b or b,c or c,a or bb or ....
{9$$a|b|c} ->  {3$$a|b|c} auto fix max count
{1-2$$a|b|c} -> 1~2 random choise
{-2$$a|b|c} -> {0-2$$a|b|c}  0-2
{1-$$a|b|c} -> {0-3$$a|b|c}  1-max
{-$$a|b|c} -> {0-3$$a|b|c}  0-max
```

### ex - wildcard text file use

- ~/a/b.txt
```
1
```
- ~/b.txt
```
2
```

- __b__ to 1 or 2
- __/b__ to 2
- __/a/b__ to 1

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



### txt file (UTF8)
from
```
# 주석 comment
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

### reload card

call wildcards.card_load()
or
wildcards.run("{9$$-$$a|b|c}",True)

## for ComfyUI



### CLIPTextEncodeWildcards

- CLIPTextEncodeWildcards : no seed
- CLIPTextEncodeWildcards : seed

![2023-03-20 02 13 50](https://user-images.githubusercontent.com/20321215/226194627-b560c9e1-5dfa-49d9-8503-939693a8b119.png)


### SimpleSampler+modelVAE

- include wildcards

![SimpleSampler+modelVAE](https://user-images.githubusercontent.com/20321215/229340970-19c5c0f7-6281-430d-87ce-c2e512ead277.png)


### SimpleSampler

- include wildcards

![SimpleSampler](https://user-images.githubusercontent.com/20321215/229341019-0cea9dd8-0b03-4f4a-8f49-aff068b58faf.png)


### SimpleSamplerVAE

- include wildcards

![SimpleSamplerVAE](https://user-images.githubusercontent.com/20321215/229341040-72d422d5-7904-41c3-a0e7-ac256ea40d0e.png)

### VAELoaderText , LoraLoaderText , CheckpointLoaderSimpleText

- support file name Wildcard(?*)

![2023-04-13 23 07 29](https://user-images.githubusercontent.com/20321215/231785743-a77257b1-6932-4713-8b91-0614aeeb45e8.png)
![2023-04-13 23 07 49](https://user-images.githubusercontent.com/20321215/231785748-b33b5d69-de00-4265-8fdb-405e61ab8758.png)


### random_sampler_node.py

![2023-03-18 20 53 37](https://user-images.githubusercontent.com/20321215/226104447-eadd1d15-437f-4a41-b989-511390236d13.png)

### VAELoaderDecode.py

![2023-03-18 20 52 27](https://user-images.githubusercontent.com/20321215/226104441-a13f49c6-c5be-4c70-b93e-f4ad984e9ff1.png)

import os, glob, sys
import random
import re
#import wildcards

print("wildcards")
#print(os.getcwd())

#mn=os.path.abspath(__main__)
#print("nm ", mn)
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


# ============================================================

# 가져올 파일 목록
card_path=os.path.dirname(__file__)+"\\..\\..\\wildcards\\**\\*.txt"
#card_path=f"{os.getcwd()}\\wildcards\\**\\*.txt"
print(f"wildcards card_path {card_path}")

# 정규식
resub  = re.compile(r"(\{)([^\{\}]*)(\})")
recard = re.compile(r"(__)(.*?)(__)")

# 카드 목록
cards = {}

# | 로 입력된것중 하나 가져오기
def sub(match):
    m=match.group(2).split("|")
    #print(f"sub : {m}")
    return random.choice(m)

# | 로 입력된것중 하나 가져오기 반복
def sub_loop(text):
    bak=text
    for i in range(1, 50):
        tmp=resub.sub(sub, bak)
        if bak==tmp :
            return tmp
        bak=tmp
    return bak

# 카드 중에서 가져오기
def card(match):
    #print(f"card i : {match.group(2)}")
    if match.group(2) in cards :
        r=random.choice(cards[match.group(2)])        
    else :    
        r= match.group(2)
    #print(f"card r : {r}")
    return r
    

# 카드 중에서 가져오기 반복. | 의 것도 처리
def card_loop(text):
    bak=text
    for i in range(1, 50):
        tmp=recard.sub(card, bak)
        #print(f"card l : {bak}")
        if bak==tmp :
            tmp=sub_loop(tmp)
            
        if bak==tmp :
            #print(f"card le : {bak}")
            return tmp
        bak=tmp
    #print(f"card le : {bak}")
    return bak
    
# 카드 파일 읽기
def card_load():
    global cards , card_path
    cards = {}
    #print(f"path : {path}")
    files=glob.glob(card_path, recursive=True)
    #print(f"files : {files}")
    
    for file in files:
        basename = os.path.basename(file)
        file_name = os.path.splitext(basename)[0]
        if not file_name in cards:
            cards[file_name]=[]
        #print(f"file_name : {file_name}")
        f = open(file, 'r', encoding='UTF8')
        lines = f.readlines()
        for line in lines:
            line=line.strip()
            # 주석 빈줄 제외
            if line.startswith("#") or len(line)==0:
                continue
            cards[file_name]+=[line]
            #print(f"line : {line}")
    print(f"cards : {len(cards)}")
    #print(f"cards : {cards.keys()}")

# 실행기
def run(text):

    card_load()

    #print(f"text : {text}")
    result=card_loop(text)
    #print(f"result : {result}")
    return result
    
# ============================================================

# 테스트용
test="__my__"

#m = p.sub(sub, test)
#print(m)

run(test)

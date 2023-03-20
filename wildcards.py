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
#resub  = re.compile(r"(\{)([^\{\}]*)(\})")
resub  = re.compile(r"(\{)(((\d+)|(\d+)?-(\d+)?)?\$\$)?([^\{\}]*)(\})")
recard = re.compile(r"(__)(.*?)(__)")

# 카드 목록
cards = {}
seperator=", "
loop_max=50

# | 로 입력된것중 하나 가져오기
def sub(match):
    #print(f"sub : {(match.groups())}")
    try:        
        #m=match.group(2)
        s=match.group(3)
        m=match.group(7).split("|")

        #print(f"m : {m}")
        if s is None:
            return random.choice(m)
        c=len(m)
        n=int(match.group(4)) if  match.group(4) else None
        if n:

            r=seperator.join(random.sample(m,min(n,c)))
            #print(f"n : {n} ; {r}")
            return r

        n1=match.group(5)
        n2=match.group(6)
        
        if n1 or n2:
            a=min(int(n1 if n1 else c), int(n2 if n2 else c),c)
            b=min(max(int(n1 if n1 else 0), int(n2 if n2 else 0)),c)
            #print(f"ab : {a} ; {b}")
            r=seperator.join(
                random.sample(
                    m,
                    random.randint(
                        a,b
                    )
                )
            )
            #n1=int(match.group(5)) if not match.group(5) is None 
            #n2=int(match.group(6)) if not match.group(6) is None 
        else:
            r=seperator.join(
                random.sample(
                    m,
                    random.randint(
                        0,c
                    )
                )
            )
        #print(f"12 : {r}")
        return r


    except Exception as e:         
        print(f"Error : {match.groups()}")
        print(f"Exception : {e}")
        return ""
        
        

# | 로 입력된것중 하나 가져오기 반복
def sub_loop(text):
    bak=text
    for i in range(1, loop_max):
        tmp=resub.sub(sub, bak)
        #print(f"tmp : {tmp}")
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
    for i in range(1, loop_max):
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

#m = p.sub(sub, test)
#print(m)
#print(__name__)
if __name__ == '__main__' :
    # 테스트용
    test="{3$$a1|{b2|c3|}|d4|{-$$|f|g}|{-2$$h||i}|{1-$$j|k|}}/{$$l|m|}/{0$$n|}"
    print(run(test))
    print(run("{9$$a|b}"))

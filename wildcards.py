import glob, sys
import random
import re
import os
if __name__ == os.path.splitext(os.path.basename(__file__))[0] or __name__ =='__main__':
    from ConsoleColor import print, console, ccolor
else:
    from .ConsoleColor import print, console , ccolor
#print(__file__)
#print(os.path.basename(__file__))
#print(os.getcwd())

import subprocess
import pkg_resources

required  = {'chardet'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing   = required - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

import chardet

# ============================================================
class wildcards:

    # 가져올 파일 목록
    card_path = os.path.join(os.path.dirname(__file__), "..", "..", "wildcards", "**", "*.txt")
    #card_path=f"{os.getcwd()}\\wildcards\\**\\*.txt"
    print(f"wildcards card_path : ", card_path , style="bold CYAN")

    # 정규식
    #resub  = re.compile(r"(\{)([^\{\}]*)(\})")
    #resub  = re.compile(r"(\{)(((\d+)|(\d+)?-(\d+)?)?\$\$((.*)?\$\$)?)?([^\{\}]*)(\})")
    resub  = re.compile(r"(\{)(((\d+)|(\d+)?-(\d+)?)?\$\$(([^\{\}]*?)\$\$)?)?([^\{\}]*)(\})")
    recard = re.compile(r"(__)(.*?)(__)")

    # 카드 목록
    is_card_Load = False
    cards = {}
    seperator=", "
    loop_max=50

    # | 로 입력된것중 하나 가져오기
    def sub(match):
        #print(f"sub : {(match.groups())}")
        try:        
            #m=match.group(2)
            seperator=wildcards.seperator
            s=match.group(3)
            m=match.group(9).split("|")
            p=match.group(8)
            if p:
                seperator=p
                
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
            console.print_exception()
            return ""
            
            

    # | 로 입력된것중 하나 가져오기 반복
    def sub_loop(text):
        bak=text
        for i in range(1, wildcards.loop_max):
            tmp=wildcards.resub.sub(wildcards.sub, bak)
            #print(f"tmp : {tmp}")
            if bak==tmp :
                return tmp
            bak=tmp
        return bak

    # 카드 중에서 가져오기
    def card(match):
        #print(f"card i : {match.group(2)}")
        if match.group(2) in wildcards.cards :
            r=random.choice(wildcards.cards[match.group(2)])        
        else :    
            r= match.group(2)
        #print(f"card r : {r}")
        return r
        

    # 카드 중에서 가져오기 반복. | 의 것도 처리
    def card_loop(text):
        bak=text
        for i in range(1, wildcards.loop_max):
            tmp=wildcards.recard.sub(wildcards.card, bak)
            #print(f"card l : {bak}")
            if bak==tmp :
                tmp=wildcards.sub_loop(tmp)
                
            if bak==tmp :
                #print(f"card le : {bak}")
                return tmp
            bak=tmp
        #print(f"card le : {bak}")
        return bak
        
    # 카드 파일 읽기
    def card_load():
        #cards=wildcards.cards
        card_path=wildcards.card_path
        cards = {}
        #print(f"path : {path}")
        files=glob.glob(card_path, recursive=True)
        #print(f"files : {files}")
        
        for file in files:
            basenameAll = os.path.basename(file)
            basename = os.path.relpath(file, os.path.dirname(__file__)).replace("\\", "/").replace("../../wildcards/", "")
            #print(f"basenameAll : {basenameAll}")
            #print(f"basename : {basename}")
            file_nameAll = os.path.splitext(basenameAll)[0]
            file_name = "/"+os.path.splitext(basename)[0]
            #print(f"file_nameAll : {file_nameAll}")
            #print(f"file_name : {file_name}")
            if not file_nameAll in cards:
                cards[file_nameAll]=[]
            if not file_name in cards:
                cards[file_name]=[]
            #print(f"file_name : {file_name}")
            with open(file, "rb") as f:
                raw_data = f.read()
                encoding = chardet.detect(raw_data)["encoding"]
            with open(file, "r", encoding=encoding) as f:
                lines = f.readlines()
                for line in lines:
                    line=line.strip()
                    # 주석 빈줄 제외
                    if line.startswith("#") or len(line)==0:
                        continue
                    cards[file_nameAll]+=[line]
                    cards[file_name]+=[line]
                    #print(f"line : {line}")
        wildcards.cards=cards
        print(f"[cyan]cards file count : [/cyan]", len(wildcards.cards))
        #print(f"cards : {cards.keys()}")
        wildcards.is_card_Load=True

    # 실행기
    def run(text,load=False):
        if text is None or not isinstance(text, str):
            print("[red]text is not str : [/red]",text)
            return None
        if not wildcards.is_card_Load or load:
            wildcards.card_load()

        #print(f"text : {text}")
        result=wildcards.card_loop(text)
        #print(f"result : {result}")
        return result
        
    # ============================================================

#m = p.sub(sub, test)
#print(m)
#print(__name__)
#if __name__ == '__main__' :
    # 테스트용
#test="{3$$a1|{b2|c3|}|d4|{-$$|f|g}|{-2$$h||i}|{1-$$j|k|}}/{$$l|m|}/{0$$n|}/{9$$-$$a|b|c}/{9$$ {and|or} $$a|b|c}"
#print("[green]wildcards test : [/green]",wildcards.run(test),style="reset")
#print("wildcards test : "+wildcards.run("{9$$a|b}"))
#print("[green]wildcards test : [/green]",wildcards.run("__my__"))
#print("wildcards test : "+wildcards.run("{9$$-$$a|b|c}"))
#print("wildcards test : "+wildcards.run("{9$$ {and|or} $$a|b|c}"))
#print("wildcards test : "+wildcards.run("{{slender,|} {nature,|} {curvy,|} {thin,|} {narrow,|} {slim,|} {mini,|} {little,|}| {|very }{-$$ $$thin|slender|narrow|slim|little|skinny|mini} body, }"))
print("wildcards test : "+wildcards.run("__test__"))
print("wildcards test : "+wildcards.run("__/test__"))
print("wildcards test : "+wildcards.run("__/0/test__"))

class Colors:
    BLACK   = '\033[30m'      #Colors.BLACK
    RED     = '\033[31m'        #Colors.BLACK
    GREEN   = '\033[32m'      #Colors.BLACK
    YELLOW  = '\033[33m'     #Colors.YELLOW
    BLUE    = '\033[34m'       #Colors.BLACK
    MAGENTA = '\033[35m'    #Colors.BLACK
    CYAN    = '\033[36m'       #Colors.BLACK
    WHITE   = '\033[37m'      #Colors.BLACK
    BBLACK   = '\033[90m'      #Colors.BLACK
    BRED     = '\033[91m'        #Colors.BLACK
    BGREEN   = '\033[92m'      #Colors.BLACK
    BYELLOW  = '\033[93m'     #Colors.YELLOW
    BBLUE    = '\033[94m'       #Colors.BLACK
    BMAGENTA = '\033[95m'    #Colors.BLACK
    BCYAN    = '\033[96m'       #Colors.BLACK
    BWHITE   = '\033[97m'      #Colors.BLACK
    UNDERLINE = '\033[4m'   #Colors.BLACK
    RESET   = '\033[0m'       #Colors.BLACK
    
def cprint(text,color=None):
    if color:
        print(color + text + Colors.RESET)
    else:
        print(text)
        
#from .Colors import cprint, Colors as Colors
import os
py_name=os.path.basename(__file__)
cprint(py_name, Colors.BLUE)
cprint("BLACK", Colors.BLACK)
cprint("RED", Colors.RED)
cprint("GREEN", Colors.GREEN)
cprint("MAGENTA", Colors.MAGENTA)
cprint("CYAN", Colors.CYAN)
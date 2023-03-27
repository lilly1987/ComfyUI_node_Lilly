import os, sys
import sys
import subprocess
import pkg_resources

required  = {'rich'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing   = required - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
    
from rich.console import Console
from rich.theme import Theme
#console=Console(style="reset")
custom_theme = Theme({
    "repr.path": "bright_blue",
    "progress.percentage": "bright_blue",
    "markdown.block_quote": "bright_blue",
    "iso8601.time": "bright_blue"
})
console = Console(theme=custom_theme)
print=console.log
"""
print("test", style="bold white on blue")
print("test", style="bold green")
print("test", style="bold CYAN")
"""
"""
import os
if __name__ == os.path.splitext(os.path.basename(__file__))[0] or __name__ =='__main__':
    from ConsoleColor import print, console
else:
    from .ConsoleColor import print, console
print(__file__)
print(os.path.basename(__file__))
"""

"""

print(
    {
        'test1':'tset',
        'test2':'tset',
    }
)
print("test", style="bold white on blue")
"""

"""
print(__file__)
print(os.path.basename(__file__))
try:
    Exception_test()
except Exception:
    #console.print_exception(show_locals=True)
    console.print_exception()
    
"""
import sys
from cx_Freeze import setup, Executable

base = None
if (sys.platform == "win32"):
    base = "Win32GUI"    # Tells the build script to hide the console.

setup(  name = "reversi2014",
        version = "0.1.0",
        description = "Reversi 2014 Alpha Build",
        # options = {"build_exe": build_exe_options},
        executables = [Executable("main.pyw", base=base)])
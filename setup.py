import sys
from cx_Freeze import setup, Executable

base = None
if (sys.platform == "win32"):
    base = "Win32GUI"    # Tells the build script to hide the console.

options = {
    'build_exe': {
        'include_msvcr': True,
        'icon': 'reversi-icon.ico',
        # 'include_files': sys.path + ['Quicksand-Light.ttf']
        'include_files': ['Quicksand-Light.ttf','reversi-icon.png']
    }
}

executables = [
    Executable("main.pyw",base=base,targetName="Reversi 2014.exe")
]

setup(  name = "Reversi 2014",
        version = "0.1.1",
        description = "Reversi 2014 Alpha Build",
        options = options,
        executables = executables
        )
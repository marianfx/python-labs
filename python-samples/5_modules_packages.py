
import this # => display the Zen of Py
# 1. Any python file can be imported as module
# to load from another module:
import sys
sys.path += ["path_to_folder"] # and import MyModule

if __name__ == "__main__":
    pass # this code will exec only if the script is ran. if loaded as module, it will not run

# PACKAGES

# MathOps               - one must define main dir for package
#     __init__.py       - must have __init__.py, it runs at dir loading
#     Simple
#         __init__.py
#       Arithmetic.py
#     Bits.py

# One can access as import MathOps.Simple or import MathOps.Bits etc.abs
# for from MathOps import * to work, one must define __all__ = ["PyFileName1", ..] (dir relative)
# can dynnamically import module with m = importlib.import_module("name")
# with exec(string) one can execute dynamic code

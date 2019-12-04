"""Simple example of loading and using the system C library from Python"""
import os
import sys, platform
import ctypes, ctypes.util

# Get the path to the system C library
#path_lib = ctypes.util.find_library("./libmylib.so")
path_lib = os.path.join(os.path.dirname(__file__),"libmylib.so")
if not path_lib:
    print("Unable to find library")
    sys.exit()



# Get a handle to the sytem C library
try:
    mylib = ctypes.CDLL(path_lib)
except OSError:
    print("Unable to load the library")
    sys.exit()

print('Succesfully loaded the library from "%s"' % path_lib)

def test_empty():
    return mylib.test_empty()

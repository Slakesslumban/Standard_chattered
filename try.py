import os
import ctypes

# Manually specify the correct C library for Windows
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
libc_name = "msvcrt.dll"  # Windows C standard library
ctypes.CDLL(libc_name)

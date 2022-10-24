import os, sys
try:
    __import__("Fbs").rmx_share()
except Exception as e:
    exit(str(e))
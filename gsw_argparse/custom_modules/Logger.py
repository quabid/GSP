#!/usr/bin/env python3

def log(obj):
    strObj = ""
    try:
        strObj = str(obj)
    except Exception:
        msg = "Error casting {var} into a String\n"
        print(msg.format(var=obj))
    print(strObj)

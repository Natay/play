import re

def is_valid_IP(strng):
    prim = [x for x in strng.split('.') if len(x) ==1]
    dprim = [x for x in strng.split('.') if '0' in x]
    if len(prim)>1: return False
    if len(dprim)>=1 and ('0' in dprim):
        if strng.index('0') == 0 or strng.index('0')== len(strng)-1:
            return False
    elif len(dprim)>=1:
        for x in dprim:
            if x[0]=='0': return False
    
    uno  = re.search(r"[1-9]+0.+[1-9]\.[1-9]+0.+[1-9]",strng)
    duo = re.search(r"[0-9]+\.[0-9]+\.[0-9]+\.[0-9]", strng)
    if uno or duo :return True
    return False

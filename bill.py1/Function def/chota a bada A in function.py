#  chot a and bada A
def str(o):
    c=ord(o)
    p=0
    if (c<97):
        p=c+32
    elif(c>96):
        p=c-32
    return p
k=str("V")
print(chr(k))
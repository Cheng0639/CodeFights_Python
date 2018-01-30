def catWalk(code):
    return " ".join(code.split())


print(catWalk("def      m   e  gaDifficu     ltFun        ction(x):")
      == "def m e gaDifficu ltFun ction(x):")
print(catWalk("      for      i      in         ra   nge(x,   29):")
      == "for i in ra nge(x, 29):")
print(catWalk("r e t u r n True") == "r e t u r n True")

import re


def newStyleFormatting(s):
    s1 = s.replace("%%", "<QWEASD>")
    s2 = re.sub
    s2 = re.sub(r'%[bcdeEfFgGnosxX]', r'{}', s1)
    return s2.replace('<QWEASD>', '%')


print("%".join([str(i) for i in range(0, 10)]))
print(newStyleFormatting("We expect the %f%% growth this week")
      == "We expect the {}% growth this week")
print(newStyleFormatting("%d%d%%-growth in products is expected quite soon")
      == "{}{}%-growth in products is expected quite soon")
print(newStyleFormatting("New style formatting (like %s) is waay cooler than old-style (i.e. %s)")
      == "New style formatting (like {}) is waay cooler than old-style (i.e. {})")
print(newStyleFormatting("Much %%s we have here!") == "Much %s we have here!")

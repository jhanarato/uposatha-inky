# Taken from this Stack Overflow question and refactored:
# https://stackoverflow.com/questions/4190667/how-to-get-width-of-a-truetype-font-character-in-1200ths-of-an-inch-with-python#61647653

from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._c_m_a_p import CmapSubtable

font = TTFont('/Library/Fonts/Arial.ttf')
cmap = font['cmap']
t = cmap.getcmap(3,1).cmap
s = font.getGlyphSet()
units_per_em = font['head'].unitsPerEm

def getTextWidth(text,pointSize):
    total = 0
    for c in text:
        if ord(c) in t and t[ord(c)] in s:
            total += s[t[ord(c)]].width
        else:
            total += s['.notdef'].width
    total = total*float(pointSize)/units_per_em;
    return total

text = 'This is a test'

width = getTextWidth(text,12)

print ('Text: "%s"' % text)
print ('Width in points: %f' % width)
print ('Width in inches: %f' % (width/72))
print ('Width in cm: %f' % (width*2.54/72))
print ('Width in WP Units: %f' % (width*1200/72))
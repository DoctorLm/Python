'查询matplotlib系统中文字体'
from matplotlib.font_manager import fontManager
import os
fonts = [font.name for font in fontManager.ttflist if os.path.exists(font.fname) and os.stat(font.fname).st_size>1e6]
for font in fonts:
    print(font)
'''.Helvetica Neue DeskInterface
    Heiti TC
    Avenir
    Arial Unicode MS
    System Font
    Devanagari Sangam MN
    Hiragino Sans
    Hiragino Sans
    Thonburi
    Songti SC
    Helvetica Neue
    .Aqua Kana
    Menlo
    System Font
    Lucida Grande
    Hiragino Sans GB
    PingFang HK
    Snell Roundhand
    Copperplate
    .SF NS Rounded
    Athelas
    Hiragino Sans
    Heiti TC
    Papyrus
    Geeza Pro
    Hoefler Text
    Hiragino Sans
    American Typewriter
    Seravek
    Charter
    Damascus
    Hiragino Maru Gothic Pro
    Hiragino Sans
    Iowan Old Style
    AppleMyungjo
    Superclarendon
    Hiragino Mincho ProN
    Hiragino Sans
    Hiragino Sans
    Palatino
    Gill Sans
    Baskerville
    Hiragino Sans
    Avenir Next
    Hiragino Sans
    Kailasa
    AppleGothic
    Apple SD Gothic Neo
    PT Serif
    Helvetica
    Cochin
    Kohinoor Devanagari
    Diwan Thuluth
    Avenir Next Condensed
    PT Sans
    Mishafi
    Hiragino Sans'''

class Font5x8:
    width = 5
    height = 8
    firstchar = 32
    lastchar = 128
    table = [
    0x00,0x00,0x00,0x00,0x00, # ' '
    0x00,0x00,0x4f,0x00,0x00, # '!'
    0x00,0x07,0x00,0x07,0x00, # '"'
    0x14,0x7f,0x14,0x7f,0x14, # '#'
    0x24,0x2a,0x7f,0x2a,0x12, # '$'
    0x23,0x13,0x08,0x64,0x62, # '%'
    0x36,0x49,0x55,0x22,0x20, # '&'
    0x00,0x05,0x03,0x00,0x00, # '''
    0x00,0x1c,0x22,0x41,0x00, # '('
    0x00,0x41,0x22,0x1c,0x00, # ')'
    0x14,0x08,0x3e,0x08,0x14, # '#'
    0x08,0x08,0x3e,0x08,0x08, # '+'
    0x50,0x30,0x00,0x00,0x00, # ','
    0x08,0x08,0x08,0x08,0x08, # '-'
    0x00,0x60,0x60,0x00,0x00, # '.'
    0x20,0x10,0x08,0x04,0x02, # '/'
    0x3e,0x51,0x49,0x45,0x3e, # '0'
    0x00,0x42,0x7f,0x40,0x00, # '1'
    0x42,0x61,0x51,0x49,0x46, # '2'
    0x21,0x41,0x45,0x4b,0x31, # '3'
    0x18,0x14,0x12,0x7f,0x10, # '4'
    0x27,0x45,0x45,0x45,0x39, # '5'
    0x3c,0x4a,0x49,0x49,0x30, # '6'
    0x01,0x71,0x09,0x05,0x03, # '7'
    0x36,0x49,0x49,0x49,0x36, # '8'
    0x06,0x49,0x49,0x29,0x1e, # '9'
    0x00,0x36,0x36,0x00,0x00, # ':'
    0x00,0x56,0x36,0x00,0x00, # ';'
    0x08,0x14,0x22,0x41,0x00, # '<'
    0x14,0x14,0x14,0x14,0x14, # '='
    0x00,0x41,0x22,0x14,0x08, # '>'
    0x02,0x01,0x51,0x09,0x06, # '?'
    0x3e,0x41,0x5d,0x55,0x1e, # '@'
    0x7e,0x11,0x11,0x11,0x7e, # 'A'
    0x7f,0x49,0x49,0x49,0x36, # 'B'
    0x3e,0x41,0x41,0x41,0x22, # 'C'
    0x7f,0x41,0x41,0x22,0x1c, # 'D'
    0x7f,0x49,0x49,0x49,0x41, # 'E'
    0x7f,0x09,0x09,0x09,0x01, # 'F'
    0x3e,0x41,0x49,0x49,0x7a, # 'G'
    0x7f,0x08,0x08,0x08,0x7f, # 'H'
    0x00,0x41,0x7f,0x41,0x00, # 'I'
    0x20,0x40,0x41,0x3f,0x01, # 'J'
    0x7f,0x08,0x14,0x22,0x41, # 'K'
    0x7f,0x40,0x40,0x40,0x40, # 'L'
    0x7f,0x02,0x0c,0x02,0x7f, # 'M'
    0x7f,0x04,0x08,0x10,0x7f, # 'N'
    0x3e,0x41,0x41,0x41,0x3e, # 'O'
    0x7f,0x09,0x09,0x09,0x06, # 'P'
    0x3e,0x41,0x51,0x21,0x5e, # 'Q'
    0x7f,0x09,0x19,0x29,0x46, # 'R'
    0x26,0x49,0x49,0x49,0x32, # 'S'
    0x01,0x01,0x7f,0x01,0x01, # 'T'
    0x3f,0x40,0x40,0x40,0x3f, # 'U'
    0x1f,0x20,0x40,0x20,0x1f, # 'V'
    0x3f,0x40,0x38,0x40,0x3f, # 'W'
    0x63,0x14,0x08,0x14,0x63, # 'X'
    0x07,0x08,0x70,0x08,0x07, # 'Y'
    0x61,0x51,0x49,0x45,0x43, # 'Z'
    0x00,0x7f,0x41,0x41,0x00, # '['
    0x02,0x04,0x08,0x10,0x20, # '\'
    0x00,0x41,0x41,0x7f,0x00, # ']'
    0x04,0x02,0x01,0x02,0x04, # '^'
    0x40,0x40,0x40,0x40,0x40, # '_'
    0x00,0x00,0x03,0x05,0x00, # '`'
    0x20,0x54,0x54,0x54,0x78, # 'a'
    0x7F,0x44,0x44,0x44,0x38, # 'b'
    0x38,0x44,0x44,0x44,0x44, # 'c'
    0x38,0x44,0x44,0x44,0x7f, # 'd'
    0x38,0x54,0x54,0x54,0x18, # 'e'
    0x04,0x04,0x7e,0x05,0x05, # 'f'
    0x08,0x54,0x54,0x54,0x3c, # 'g'
    0x7f,0x08,0x04,0x04,0x78, # 'h'
    0x00,0x44,0x7d,0x40,0x00, # 'i'
    0x20,0x40,0x44,0x3d,0x00, # 'j'
    0x7f,0x10,0x28,0x44,0x00, # 'k'
    0x00,0x41,0x7f,0x40,0x00, # 'l'
    0x7c,0x04,0x7c,0x04,0x78, # 'm'
    0x7c,0x08,0x04,0x04,0x78, # 'n'
    0x38,0x44,0x44,0x44,0x38, # 'o'
    0x7c,0x14,0x14,0x14,0x08, # 'p'
    0x08,0x14,0x14,0x14,0x7c, # 'q'
    0x7c,0x08,0x04,0x04,0x00, # 'r'
    0x48,0x54,0x54,0x54,0x24, # 's'
    0x04,0x04,0x3f,0x44,0x44, # 't'
    0x3c,0x40,0x40,0x20,0x7c, # 'u'
    0x1c,0x20,0x40,0x20,0x1c, # 'v'
    0x3c,0x40,0x30,0x40,0x3c, # 'w'
    0x44,0x28,0x10,0x28,0x44, # 'x'
    0x0c,0x50,0x50,0x50,0x3c, # 'y'
    0x44,0x64,0x54,0x4c,0x44, # 'z'
    0x08,0x36,0x41,0x41,0x00, # '{'
    0x00,0x00,0x77,0x00,0x00, # '|'
    0x00,0x41,0x41,0x36,0x08, # '}'
    0x08,0x08,0x2a,0x1c,0x08, # '<-'
    0x08,0x1c,0x2a,0x08,0x08, # '->'
    0x7f,0x49,0x49,0x49,0x36, # 'BTC'
    ]

class Font7x8:
    width = 7
    height = 8
    firstchar = 32
    lastchar = 128
    table = [
     0,   0,   0,   0,   0,   0,   0, # ' '
     0,   6,  95,  95,   6,   0,   0, # '!'
     0,   7,   7,   0,   7,   7,   0, # '"'
    20, 127, 127,  20, 127, 127,  20, # '#'
    36,  46, 107, 107,  58,  18,   0, # '$'
    70, 102,  48,  24,  12, 102,  98, # '%'
    48, 122,  79,  93,  55, 122,  72, # '&'
     4,   7,   3,   0,   0,   0,   0, # '''
     0,  28,  62,  99,  65,   0,   0, # '('
     0,  65,  99,  62,  28,   0,   0, # ')'
     8,  42,  62,  28,  28,  62,  42, # '*'
     8,   8,  62,  62,   8,   8,   0, # '+'
     0, 128, 224,  96,   0,   0,   0, # ','
     8,   8,   8,   8,   8,   8,   0, # '-'
     0,   0,  96,  96,   0,   0,   0, # '.'
    96,  48,  24,  12,   6,   3,   1, # '/'
    62, 127, 113,  89,  77, 127,  62, # '0'
    64,  66, 127, 127,  64,  64,   0, # '1'
    98, 115,  89,  73, 111, 102,   0, # '2'
    34,  99,  73,  73, 127,  54,   0, # '3'
    24,  28,  22,  83, 127, 127,  80, # '4'
    39, 103,  69,  69, 125,  57,   0, # '5'
    60, 126,  75,  73, 121,  48,   0, # '6'
     3,   3, 113, 121,  15,   7,   0, # '7'
    54, 127,  73,  73, 127,  54,   0, # '8'
     6,  79,  73, 105,  63,  30,   0, # '9'
     0,   0, 102, 102,   0,   0,   0, # ':'
     0, 128, 230, 102,   0,   0,   0, # ';'
     8,  28,  54,  99,  65,   0,   0, # '<'
    36,  36,  36,  36,  36,  36,   0, # '='
     0,  65,  99,  54,  28,   8,   0, # '>'
     2,   3,  81,  89,  15,   6,   0, # '?'
    62, 127,  65,  93,  93,  31,  30, # '@'
    124,126,  19,  19, 126, 124,   0, # 'A'
    65, 127, 127,  73,  73, 127,  54, # 'B'
    28,  62,  99,  65,  65,  99,  34, # 'C'
    65, 127, 127,  65,  99,  62,  28, # 'D'
    65, 127, 127,  73,  93,  65,  99, # 'E'
    65, 127, 127,  73,  29,   1,   3, # 'F'
    28,  62,  99,  65,  81, 115, 114, # 'G'
    127,127,   8,   8, 127, 127,   0, # 'H'
     0,  65, 127, 127,  65,   0,   0, # 'I'
    48, 112,  64,  65, 127,  63,   1, # 'J'
    65, 127, 127,   8,  28, 119,  99, # 'K'
    65, 127, 127,  65,  64,  96, 112, # 'L'
    127,127,  14,  28,  14, 127, 127, # 'M'
    127,127,   6,  12,  24, 127, 127, # 'N'
    28,  62,  99,  65,  99,  62,  28, # 'O'
    65, 127, 127,  73,   9,  15,   6, # 'P'
    30,  63,  33, 113, 127,  94,   0, # 'Q'
    65, 127, 127,   9,  25, 127, 102, # 'R'
    38, 111,  77,  89, 115,  50,   0, # 'S'
     3,  65, 127, 127,  65,   3,   0, # 'T'
    127,127,  64,  64, 127, 127,   0, # 'U'
    31,  63,  96,  96,  63,  31,   0, # 'V'
    127,127,  48,  24,  48, 127, 127, # 'W'
    67, 103,  60,  24,  60, 103,  67, # 'X'
     7,  79, 120, 120,  79,   7,   0, # 'Y'
    71,  99, 113,  89,  77, 103, 115, # 'Z'
     0, 127, 127,  65,  65,   0,   0, # '['
     1,   3,   6,  12,  24,  48,  96, # '\'
     0,  65,  65, 127, 127,   0,   0, # ']'
     8,  12,   6,   3,   6,  12,   8, # '^'
    128,128, 128, 128, 128, 128, 128, # '_'
     0,   0,   3,   7,   4,   0,   0, # '`'
    32, 116,  84,  84,  60, 120,  64, # 'a'
    65, 127,  63,  72,  72, 120,  48, # 'b'
    56, 124,  68,  68, 108,  40,   0, # 'c'
    48, 120,  72,  73,  63, 127,  64, # 'd'
    56, 124,  84,  84,  92,  24,   0, # 'e'
    72, 126, 127,  73,   3,   2,   0, # 'f'
    56, 188, 164, 164, 252, 120,   0, # 'g'
    65, 127, 127,   8,   4, 124, 120, # 'h'
     0,  68, 125, 125,  64,   0,   0, # 'i'
    96, 224, 128, 128, 253, 125,   0, # 'j'
    65, 127, 127,  16,  56, 108,  68, # 'k'
     0,  65, 127, 127,  64,   0,   0, # 'l'
    120,124,  28,  56,  28, 124, 120, # 'm'
    124,124,   4,   4, 124, 120,   0, # 'n'
    56, 124,  68,  68, 124,  56,   0, # 'o'
    0,  252, 252, 164,  36,  60,  24, # 'p'
    24,  60,  36, 164, 248, 252, 132, # 'q'
    68, 124, 120,  76,   4,  28,  24, # 'r'
    72,  92,  84,  84, 116,  36,   0, # 's'
     0,   4,  62, 127,  68,  36,   0, # 't'
    60, 124,  64,  64,  60, 124,  64, # 'u'
    28,  60,  96,  96,  60,  28,   0, # 'v'
    60, 124, 112,  56, 112, 124,  60, # 'w'
    68, 108,  56,  16,  56, 108,  68, # 'x'
    60, 188, 160, 160, 252, 124,   0, # 'y'
    76, 100, 116,  92,  76, 100,   0, # 'z'
     8,   8,  62, 119,  65,  65,   0, # '{'
     0,   0,   0, 119, 119,   0,   0, # '|'
    65,  65, 119,  62,   8,   8,   0, # '}'
     2,   3,   1,   3,   2,   3,   1, # '~'
    255,129, 129, 129, 129, 129, 255, # ' '
    65, 127, 127,  73,  73, 127,  54, # 'BTC'
    ]

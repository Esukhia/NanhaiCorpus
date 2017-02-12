#!/usr/bin/env python
# renaming files

import re
import os
import codecs

for file in os.listdir('./Regex/input'):
    # print(file.encode("utf-8-sig"))
    # check the encoding
    try:
        with codecs.open('./Regex/input/' + file, 'r', 'utf-8') as f:
            current_file = f.read()
    except:
        with codecs.open('./Regex/input/' + file, 'r', 'utf-16') as f:
            current_file = f.read()

    # output results
    name = 'utf-16_'
    with codecs.open('./Regex/output/' + file, 'w', 'utf-16') as f:
        f.write(current_file)

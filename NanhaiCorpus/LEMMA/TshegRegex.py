#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import re
import os

for file in os.listdir('/home/dirk/Desktop/python/Regex/input'):
    print(file)
    # check the encoding
    try:
        with codecs.open('/home/dirk/Desktop/python/Regex/input/' + file, 'r', 'utf-8') as f:
            current_file = f.read()
    except:
        with codecs.open('/home/dirk/Desktop/python/Regex/input/' + file, 'r', 'utf-16') as f:
            current_file = f.read()

    # regex list
    regexes = [
                
                (r'་ ས་ ', r' ས-P '),
                (r'་ ', r' '),
                (r'་ ', r' '),
                (r' ངས།', r' ས-i_ངས །'),
                (r' ངས ', r' ང ས '),
                (r'་།', r' །'),
                (r'། ', r' ། ')

              ]

    # apply regexes
    for regex in regexes:
        current_file = re.sub(regex[0], regex[1], current_file)
    
    # output results
    pre = 'un-tsheged_'
    with codecs.open('/home/dirk/Desktop/python/Regex/output/'+file, 'w', 'utf-8') as f:
        f.write(current_file)

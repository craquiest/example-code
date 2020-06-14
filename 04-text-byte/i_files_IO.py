# coding: utf-8
# open('cafe.txt', 'w', encoding='utf_8').write('café')
# open('cafe.txt').read() #+ this leads to bugs, always specify the encoding

fp= open('04-text-byte/cafe.txt', 'w', encoding='utf_8')
fp.write('café')
fp.close()

import os
os.stat('04-text-byte/cafe.txt').st_size
fp2= open('04-text-byte/cafe.txt')
fp2
fp2.encoding
fp2.read()

fp3= open('04-text-byte/cafe.txt',encoding='utf_8')
fp3
fp3.read()

fp4= open('04-text-byte/cafe.txt','rb')
fp4
fp4.read()

'''
to run the following shell command from inside python, prepend '!':

!code 04-text-byte/i_files_IO.py

!python 04-text-byte/default_encodings.py > 04-text-byte/encodings.log

'''


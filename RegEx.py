# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 08:41:52 2018

@author: Code Killa
"""

import nltk
import re
nltk.download()
selection = 'a'

while (selection != 'q'):
        print( '\n' )
        print( '(a) Load Angela\'s Ashes Text' )
        print( '(b) Load Pet Diary Text' )
        print( '(c) the' )
        print( '(d) [tT]he' )
        print( '(e) Enter a Pattern' )
        print( '(q) Quit' )
        selection = input('Enter a selection:  ')
        print( '\n' )

        if (selection == 'a'):
                # Load Angela's Ashes
                print( 'Loading Angela\'s Ashes' )
                filehandle = open('AngelasAshes.txt', 'r')
                text = filehandle.read()
                tokens = nltk.word_tokenize(text)
                filehandle.close()

        elif (selection == 'b'):
                # Load Pet Diary
                print( 'Loading Pet Diary' )
                filehandle = open('PetDiary.txt', 'r')
                text = filehandle.read()
                tokens = nltk.word_tokenize(text)
                filehandle.close()

        elif (selection == 'c'):
                # the
                print( 'Looking for "the"' )
                found = [w for w in tokens if re.search(r'\bthe\b', w)]
                print( 'length of "the" found:  ', len(found) )
                print( found )

        elif (selection == 'd'):
                # [tT]he
                print( 'Looking for "[tT]he"' )
                found = [w for w in tokens if re.search(r'\b[tT]he\b', w)]
                print( 'length of "[tT]he" found:  ', len(found) )
                print( found )

        elif (selection == 'e'):
                # User entered pattern
                pattern = input('Enter the Pattern:  ')
                found = [w for w in tokens if re.search(pattern, w)]
                print( 'length of ' + pattern + ' found:  ', len(found) )
                print( found )

print( 'Goodbye.' )
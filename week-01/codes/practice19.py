''' List Analysis
Write a function that takes a sentence and returns a dictionary where each word is a key and its frequency is the value. 
It should be case insensitive and ignore punctuation .,!?.
'''

import pprint

sentence='''before you can do anything. Like a wizard-in-training, you might think 
these concepts seem arcane and tedious, but with some knowledge and 
practice, you’ll be able to command your computer like a magic wand to 
perform incredible feats. 
This chapter has a few examples that encourage you to type into the 
interactive shell, which lets you execute Python instructions one at a time 
and shows you the results instantly. Using the interactive shell is great for 
learning what basic Python instructions do, so give it a try as you follow 
along. You’ll remember the things you do much better than the things 
you only read. '''

def wordCount(phrase):
    lst=phrase.lower().split()
    repetition={}
    for item in lst:
        for char in '.,!?':
            item=item.replace(char, '')

        repetition.setdefault(item, 0)
        repetition[item]+=1
    return repetition
pprint.pprint(wordCount(sentence))


#Corrections: Used replace method and a loop using a string.
'''
Used for getting words of a certain gramatical type.

Would ideally read in data from disk, but hard to find any lists of words by
grammatical type. Most seem to be just long lists of words (similar to
/usr/share/dict/words.
'''

import random

grammar_types = {}

def populate(filename):
    '''
    Populates with all the words that can be used.

    TODO: implement for real
    '''
    grammar_types = {
        'adjective' : ['blue', 'hot', 'chilly'],
        'adverb' : ['hastily'],
        'noun' : ['table', 'rose'],
        'preposition' : ['with', 'in', 'on'],
        'pronoun' : ['he', 'she', 'it'],
        'verb' : ['sees', 'eyes'],
        }


def get_word(grammar_type):
    '''
    Gets a word of the grammar type specified.
    '''
    word_list = grammar_types[grammar_type]
    return word_list[random.randint(0, len(word_list)-1)]



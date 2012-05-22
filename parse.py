import ply.yacc as yacc             #@UnresolvedImport

import templator


class InvalidLine(Exception):
    def __init__(self, line = None):
        self.line = line
    def __str__(self):
        if self.line is None:
            return "Invalid Line"
        else:
            return "Invalid Line: #%s" % self.line


# Get the token map from the lexer.  This is required.
from lex import tokens

def p_start(p):
    '''
    start :   start adjective
            | start adverb
            | start noun
            | start preposition
            | start pronoun
            | start verb
            | empty
    '''
    if len(p) == 3:
        p[0] = '%s %s' % (p[1], templator.get_word(p[2]))
    else:
        p[0] = ''


def p_adjective(p):
    'adjective : ADJECTIVE'
    p[0] = 'adjective'


def p_adverb(p):
    'adverb : ADVERB'
    p[0] = 'adverb'


def p_noun(p):
    'noun : NOUN'
    p[0] = 'noun'


def p_preposition(p):
    'preposition : PREPOSITION'
    p[0] = 'preposition'


def p_pronoun(p):
    'pronoun : PRONOUN'
    p[0] = 'pronoun'


def p_verb(p):
    'verb : VERB'
    p[0] = 'verb'


def p_empty(p):
    'empty :'
    pass


# Error rule for syntax errors
def p_error(p):
#    print("Syntax error in input!", p)
    if p is not None:
        raise InvalidLine(p)

# Build the parser
parser = yacc.yacc()


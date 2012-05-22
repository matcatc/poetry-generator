
import ply.lex as lex       #@UnresolvedImport


tokens = [
    'ADJECTIVE',
    'ADVERB',
    'NOUN',
    'PREPOSITION',
    'PRONOUN',
    'VERB',
]


t_ADJECTIVE = r'(adjective|adj)'
t_ADVERB = r'(adverb|adv)'
t_NOUN = r'noun'
t_PREPOSITION = r'(preposition|prep)'
t_PRONOUN = r'(pronoun|pn)'
t_VERB = r'verb'


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t\n\r'


# Error handling rule
def t_error(t):
    print ("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)



lexer = lex.lex()



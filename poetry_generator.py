#!/usr/bin/python3
'''
Program which algorithmically produces a "poem" given certain input by the
user.

Ex:
    pronoun verb adjective pronoun
produces:
    he eyes blue her

It would basically be the reverse of parsing with a CFG. I.e: A template where
the words are replaced randomly. Of course we'd want to allow the user to set
and see which seed was used so we could reproduce the poem.

Might be worthwhile to use a CFG for this.
'''

import parse

def main():
    '''
    '''
    template = input('template: ')

    print("DEBUG: template = %r" % template)

    result = parse.parser.parse(template).strip()

    print("DEBUG: result = %r" % result)


if __name__ == '__main__':
    main()

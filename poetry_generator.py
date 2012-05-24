#!/usr/bin/python3
'''
Program which algorithmically produces a "poem" given certain input by the
user.

Ex:
    pronoun verb adjective pronoun
produces:
    he eyes blue her

A template where the words are replaced randomly. Of course we'd want to allow
the user to set and see which seed was used so we could reproduce the poem.

TODO: program options and config file?
'''

import random
import sys



NO_ERROR = 0
SYSTEM_ERROR = 1
USER_ERROR = 2



cannon_name = {}
grammar_list = {}


def get_cannonical_name(grammar_name):
    '''
    Retrieves the cannoncial name for the specified grammar name.
    '''
    try:
        return cannon_name[grammar_name]
    except KeyError:
        print('ERROR: unknown grammar name: %s' % grammar_name)
        sys.exit(USER_ERROR)


def random_word(word):
    '''
    Gets a random word for the specified grammar name.

    The grammar name doesn't have to be the cannonical version, it will be
    cannonicalized as part of this function.
    '''
    cannon_name = get_cannonical_name(word)
    try:
        word_list = grammar_dict[cannon_name]
    except KeyError:
        print('ERROR: unkown grammar name: %s' % cannon_name)
        sys.exit(USER_ERROR)

    try:
        return random.choice(word_list)
    except IndexError:
        print('ERROR: no replacement words for grammar name: %s' % cannon_name)
        sys.exit(USER_ERROR)
    

def create_cannonical_name_dict(filename):
    '''
    Reads in the specified file and extracts the grammar name cannonicalization
    data.

    File should be of the form:
        name -> cannonical_name
        name -> cannonical_name
    '''
    cannonical_name = {}

    with open(filename, 'r') as spec_file:
        for line in spec_file:
            if line.strip() != '':
                split_list = line.split('->')
                if len(split_list) != 2:
                    print('ERROR: line %r malformed' % line)
                    sys.exit(USER_ERROR)
                key = split_list[0].strip()
                cannon = split_list[1].strip()

                cannonical_name[key] = cannon

    return cannonical_name


def create_grammar_dict(cannon_name_list):
    '''
    Creates the grammar -> word list dictionary.

    Assumes the filenames for the wordlist. Should be cannonical_name.wordlist.
    We can change this later to be configurable, but its fine for now.
    '''
    grammar_dict = {}
    for cannon_name in cannon_name_list:
        filename = '%s.wordlist' % cannon_name
        word_list = create_word_list(filename)
        grammar_dict[cannon_name] = word_list
    return grammar_dict


def create_word_list(filename):
    '''
    Returns a word list from the provided file.

    Each word in the file must be on a separate line.

    TODO: filename doesn't exist exception
    '''
    return [line.strip() for line in open(filename, 'r')]


def main():
    '''
    '''
    global cannon_name, grammar_dict

    print('DEBUG: populating data')
    cannon_name = create_cannonical_name_dict('cannonicalization.config')

    print('DEBUG: cannon_name = %r' % cannon_name)

    grammar_dict = create_grammar_dict(set(cannon_name.values()))

    template = input('template: ')

    print("DEBUG: template = %r" % template)

    output = ''
    for line in template.splitlines():
        for word in line.split():
            output = '%s %s' % (output, random_word(word))
        output = '%s\n' % output
    output = output.strip()

    print("DEBUG: output = %r" % output)


if __name__ == '__main__':
    main()

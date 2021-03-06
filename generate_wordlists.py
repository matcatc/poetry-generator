#!/usr/bin/python3
'''
Creates the wordlists.

This particular version uses wordlist and /usr/share/dict/words to generate the
word lists.

TODO: program options (later)
    specify master_wordlist
    quiet/verbose option


@license
    This file is part of Poetry Generator.

    Poetry Generator is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the Free
    Software Foundation, either version 3 of the License, or (at your option)
    any later version.

    Poetry Generator is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
    or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
    for more details.

    You should have received a copy of the GNU General Public License along
    with Poetry Generator. If not, see <http://www.gnu.org/licenses/>.


@author Matthew Todd
@date Jun 2, 2012
'''

import re
import subprocess

master_wordlist = '/usr/share/dict/words'
#master_wordlist = './test_words'

class MyDict:
    '''
    Dictionary which will create empty lists for new keys automatically.
    '''
    def __init__(self):
        self.d = {}

    def __getitem__(self, key):
        if key not in self.d:
            self.d[key] = []
        return self.d[key]

    def keys(self):
        return self.d.keys()
        

def call_wordnet(word):
    '''
    Gets the output of wordnet for the given word.
    '''
    with subprocess.Popen(['wordnet', word], stdout=subprocess.PIPE) as proc:
        (stdout, _) = proc.communicate()

    return stdout.decode()


def get_categories(word):
    '''
    Gets the categories a word falls into.
    '''
    wordnet_output = call_wordnet(word)

    categories = []
    for line in wordnet_output.splitlines():
        line = line.strip()
        if line != '':
            matches = re.search(r'Information available for (\w+)' , line)
            if matches is not None:
                categories.append(matches.group(1))

    return categories 
        

def build_dict():
    '''
    Builds the category dictionary.

    Mapping from category to a list of all words in that category (words that
    were present in the master list.)
    '''
    cat_dictionary = MyDict()
    word_count = 0

    with open(master_wordlist, 'r') as wordlist:
        for word in wordlist:
            word = word.strip()

            for category in get_categories(word):
                cat_dictionary[category].append(word)

            word_count += 1
            # TODO: quiet/verbose option
            print('words processed: %s\r' % word_count, end='')

    print('words processed: %s' % word_count)

    return cat_dictionary


def write_wordlists(cat_dictionary):
    '''
    Writes out the wordlists using the lists provided in the dictionary.
    '''
    for category in cat_dictionary.keys():
        word_list = cat_dictionary[category]
        word_string = '\n'.join(word_list)
        word_string = '%s\n' % word_string

        filename = '%s.wordlist' % category
        with open(filename, 'w') as wordlist_file:
            print('writing %s' % filename)
            wordlist_file.write(word_string)


def main():
    '''
    '''
    cat_dictionary = build_dict()

    write_wordlists(cat_dictionary)


if __name__ == '__main__':
    main()


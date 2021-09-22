#!/usr/bin/env python3
"""
Author : hbuell6 <hbuell6@localhost>
Date   : 2021-09-20
Purpose: Teach me to sing
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Teach me to sing',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', nargs='+', help='write text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    solfege = {
        'Do': 'A deer, a female deer',
        'Re': 'A drop of golden sun',
        'Mi': 'A name I call myself',
        'Fa': 'A long long way to run',
        'Sol': 'A needle pulling thread',
        'La': 'A note to follow sol',
        'Ti': 'A drink with jam and bread'
    }
    new_text = []

    for syllable in args.text:
        if syllable in solfege:
            print(syllable + ',', solfege[syllable])
        else:
            print('I don\'t know "{}"'.format(syllable))

    print(''.join(new_text), end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()

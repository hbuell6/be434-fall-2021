#!/usr/bin/env python3
"""
Author : hbuell6 <hbuell6@localhost>
Date   : 2021-11-09
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    seqs_list = []
    for seq in args.file:
        seqs_list.append(seq.rstrip())
        print(seq, end='')
    match = ''
    for i in range(len(seqs_list[0])):
        bases = []
        for seq in seqs_list:
            bases += seq[i]
        if len(set(bases)) == 1:
            match += '|'
        else:
            match += 'X'

    print(match)


# --------------------------------------------------
if __name__ == '__main__':
    main()

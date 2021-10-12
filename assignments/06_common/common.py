#!/usr/bin/env python3
"""
Author : hbuell6 <hbuell6@localhost>
Date   : 2021-10-12
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE1',
                        help='Input file 1',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    parser.add_argument('FILE2',
                        help='Input file 2',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'))

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    words1 = {}
    for line in args.FILE1:
        for word in line.split():
            words1[word] = 1

    words2 = {}
    for line in args.FILE2:
        for word in line.split():
            words2[word] = 1

    for key in words1:
        if key in words2:
            print(key)


# --------------------------------------------------
if __name__ == '__main__':
    main()

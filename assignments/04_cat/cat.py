#!/usr/bin/env python3
"""
Author : hbuell6 <hbuell6@localhost>
Date   : 2021-09-27
Purpose: Concatenate files
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Concatenate files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'),
                        help='Input file(s)')

    parser.add_argument('-n',
                        '--number',
                        help='whether to print line numbers',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    number = args.number

    for fh in args.files:
        for number, line in enumerate(fh, start=1):
            if args.number:
                print(number, line, end='')
            else:
                print(line, end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()

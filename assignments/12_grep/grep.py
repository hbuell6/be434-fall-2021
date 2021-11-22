#!/usr/bin/env python3
"""
Author : hbuell6 <hbuell6@localhost>
Date   : 2021-11-18
Purpose: Rock the Casbah
"""

import argparse
import sys
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern', metavar='PATTERN', help='Search pattern')

    parser.add_argument('files',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case insensitive',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for fh in args.files:
        for line in fh:
            if args.insensitive:
                grep = re.search(args.pattern, line, re.I)
                name = f'{fh.name}:' if len(args.files) > 1 else ''
                print(name + line.rstrip(),
                      file=args.outfile) if grep is not None else ''
            else:
                grep = re.search(args.pattern, line)
                name = f'{fh.name}:' if len(args.files) > 1 else ''
                print(name + line.rstrip(),
                      file=args.outfile) if grep is not None else ''


# --------------------------------------------------
if __name__ == '__main__':
    main()

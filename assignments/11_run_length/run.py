#!/usr/bin/env python3
"""
Author : hbuell6 <hbuell6@localhost>
Date   : 2021-11-16
Purpose: Run-length encoding/data compression
"""

import argparse
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Run-length encoding/data compression',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq', metavar='str', help='DNA text or file')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for seq in args.seq.splitlines():
        print(rle(seq))


# --------------------------------------------------
def rle(seq):
    run = (re.findall(r'((\w)\2*)', seq))
    new_seq = ''
    for seq in run:
        for i, base in enumerate(seq):
            countA = base.count('A')
            countC = base.count('C')
            countG = base.count('G')
            countT = base.count('T')
            if countA > 1:
                num = str(countA)
            if countC > 1:
                num = str(countC)
            if countG > 1:
                num = str(countG)
            if countT > 1:
                num = str(countT)
            if i % 2 == 1:
                new_seq += base
                new_seq += num
    return(''.join(new_seq))


# --------------------------------------------------
if __name__ == '__main__':
    main()

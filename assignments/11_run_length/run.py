#!/usr/bin/env python3
"""
Author : hbuell6 <hbuell6@localhost>
Date   : 2021-11-16
Purpose: Run-length encoding/data compression
"""

import argparse
import re
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Run-length encoding/data compression',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq', metavar='str', help='DNA text or file')

    args = parser.parse_args()

    if os.path.isfile(args.seq):
        args.seq = open(args.seq).read()

    return args


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
    for seq, _ in run:
        count = str(len(seq) if len(seq) > 1 else '')
        for acgt in set(seq):
            base = acgt
            new_seq += (base + count)
    return (''.join(new_seq))


# --------------------------------------------------
def test_rle():
    """ Test rle """

    assert rle('A') == 'A'
    assert rle('ACGT') == 'ACGT'
    assert rle('AA') == 'A2'
    assert rle('AAAAA') == 'A5'
    assert rle('ACCGGGTTTT') == 'AC2G3T4'


# --------------------------------------------------
if __name__ == '__main__':
    main()

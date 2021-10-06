#!/usr/bin/env python3
"""
Author : hbuell6 <hbuell6@localhost>
Date   : 2021-10-03
Purpose: Rock the Casbah
"""

import argparse
from pprint import pprint


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence', metavar='str', help='DNA/RNA sequence')

    parser.add_argument('-c',
                        '--codons',
                        help='A file with codon translations',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        required=True,
                        default=None)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.txt')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    codon_table = {}
    for line in args.codons:
        codon, amino = line.upper().rstrip().split()
        codon_table[codon] = amino

    k = 3
    seq = args.sequence
    for codon in [seq[i:i + k] for i in range(0, len(seq), k)]:
        args.outfile.write(codon_table.get(codon, '-'))

    print(f'Output written to "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()

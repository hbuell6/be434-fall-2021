#!/usr/bin/env python3
"""
Author : hbuell6 <hbuell6@localhost>
Date   : 2021-10-29
Purpose: Split interleaved/paired reads
"""

import argparse
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Split interleaved/paired reads',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('fasta',
                        help='input FASTA files',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        type=str,
                        default='split')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    reader = SeqIO.parse(args.fasta, 'fasta')
    for rec in reader:
        print('ID :', rec.id)
        print('Seq:', str(rec.seq))


# --------------------------------------------------
if __name__ == '__main__':
    main()

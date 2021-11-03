#!/usr/bin/env python3
"""
Author : hbuell6 <hbuell6@localhost>
Date   : 2021-10-29
Purpose: Split interleaved/paired reads
"""

import argparse
from Bio import SeqIO
import os


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
                        type=argparse.FileType('rt'))

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
    out_dir = args.outdir

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    for fh in args.fasta:
        root, ext = (os.path.splitext(os.path.basename(fh.name)))
        forward = open(os.path.join(out_dir, root + '_1' + ext), 'wt')
        reverse = open(os.path.join(out_dir, root + '_2' + ext), 'wt')
        reader = SeqIO.parse(fh, 'fasta')

        for i, rec in enumerate(reader):
            out_fh = forward if i % 2 == 0 else reverse
            print(f'>{rec.id}', file=out_fh)
            print(rec.seq, file=out_fh)

    print(f'Done, see output in "{out_dir}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()

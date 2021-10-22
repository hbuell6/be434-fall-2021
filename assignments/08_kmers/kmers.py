#!/usr/bin/env python3
"""
Author : hbuell6 <hbuell6@localhost>
Date   : 2021-10-21
Purpose: Find common kmers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common kmers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file1',
                        help='Input file 1',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    parser.add_argument('file2',
                        help='Input file 2',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    parser.add_argument('-k',
                        '--kmer',
                        help='Length of kmer',
                        metavar='int',
                        type=int,
                        default=3)

    args = parser.parse_args()

    if args.kmer < 1:
        parser.error(f'--kmer "{args.kmer}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    words1 = {}
    for line in args.file1:
        for word in line.split():
            for kmer in find_kmers(word, args.kmer):
                if kmer in words1:
                    words1[kmer] += 1
                else:
                    words1[kmer] = 1

    words2 = {}
    for line in args.file2:
        for word in line.split():
            for kmer in find_kmers(word, args.kmer):
                if kmer in words2:
                    words2[kmer] += 1
                else:
                    words2[kmer] = 1

    for kmer in words1:
        if kmer in words2:
            print(f'{kmer:10} {words1.get(kmer):5} {words2.get(kmer):5}')


# --------------------------------------------------
def find_kmers(seq, k):
    """ Find k-mers in string """

    n = len(seq) - k + 1
    return [] if n < 1 else [seq[i:i + k] for i in range(n)]


# --------------------------------------------------
if __name__ == '__main__':
    main()

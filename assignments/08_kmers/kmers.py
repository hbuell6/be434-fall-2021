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

    def find_kmers(seq, k):
        """ Find k-mers in string """

        n = len(seq) - k + 1
        return [] if n < 1 else [seq[i:i + k] for i in range(n)]

    def test_find_kmers():
        """ Test find_kmers """

        assert find_kmers('', 1) == []
        assert find_kmers('ACTG', 1) == ['A', 'C', 'T', 'G']
        assert find_kmers('ACTG', 2) == ['AC', 'CT', 'TG']
        assert find_kmers('ACTG', 3) == ['ACT', 'CTG']
        assert find_kmers('ACTG', 4) == ['ACTG']
        assert find_kmers('ACTG', 5) == []


# --------------------------------------------------
if __name__ == '__main__':
    main()

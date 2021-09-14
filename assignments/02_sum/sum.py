#!/usr/bin/env python3
"""
Author : hbuell6 <hbuell6@localhost>
Date   : 2021-09-14
Purpose: Add numbers
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='add numbers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('numbers',
                        help='numbers to add',
                        metavar='int',
                        nargs= '+',
                        type=int,)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    numbers = args.numbers
    strings = [str(x) for x in numbers]
    total = sum(numbers)
    print("{} = {}".format(' + '.join(str(x)for x in numbers) , total))
    


# --------------------------------------------------
if __name__ == '__main__':
    main()

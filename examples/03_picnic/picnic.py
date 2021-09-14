#!/usr/bin/env python3
"""
Author : hbuell6 <hbuell6@localhost>
Date   : 2021-09-13
Purpose: Have a Picnic
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Have a Picnic',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        nargs='+',
                        help='items to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.items

    if args.sorted:
        items.sort()

    if len(items) == 1:
        print('You are bringing ' + items[0] + '.')
    elif len(items) == 2:
        print('You are bringing ' + items[0] + ' and ' + items[1] + '.')
    else:
        print('You are bringing ' + ', '.join(items[:-1]) + ', and ' + items[-1] + '.')
        
    
# --------------------------------------------------
if __name__ == '__main__':
    main()

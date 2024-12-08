#! /usr/bin/env python3
"""
Author: KimDaegyo <eory96@gmail.com>
purpose : say hello
"""

import argparse


def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name',
                        default='World', help='Name to greet')
    return parser.parse_args()


def main():
    """Make a jazz noise here"""
    args = get_args()
    #print('Hello {}!'.format(args.name))
    print('Hello, ' + args.name + '!')

if __name__ == '__main__':
    main()

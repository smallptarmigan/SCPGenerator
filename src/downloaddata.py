# coding=utf-8

import argparse
import os

def main(args):
    output_dir = args.output_dir
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_dir', type=str, default='./data/scp/',
                        help='directory for saving scp data')
    args = parser.parse_args()
    main(args)

import argparse
from gendiff import gendiff


parser = argparse.ArgumentParser(
    prog='gendiff',
    description='Compares two configuration files and shows a difference.'
)

parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', help='set format of output')

args = parser.parse_args()

diff = gendiff.generate_diff(args.first_file, args.second_file)


def main():
    print(diff)


if __name__ == '__main__':
    main()

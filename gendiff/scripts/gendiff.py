import argparse


parser = argparse.ArgumentParser(
    prog='gendiff',
    description='Compares two configuration files and shows a difference.'
)

parser.add_argument('first_file')
parser.add_argument('second_file')

args = parser.parse_args()

def main():
    print(args.accumulate(args.integers))


if __name__ == '__main__':
    main()

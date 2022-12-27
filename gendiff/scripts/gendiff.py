from gendiff.parser import files
from gendiff.gendiff import generate_diff


def main():
    return generate_diff(*files)


if __name__ == '__main__':
    main()

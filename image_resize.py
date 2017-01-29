import argparse
import sys

def resize_image(path_to_original, path_to_result):
    pass


def read_args():

    args_parser = argparse.ArgumentParser(prog="Image resizer")
    args_parser.add_argument("image_file_name", type=argparse.FileType('r'), nargs='*',
                             help="Image for resize", default=sys.stdin)
    args_parser.add_argument('-o', '--output' , type=argparse.FileType('w'), help='output path for new file')
    args_parser.add_argument('-s', '--scale', nargs='?', type = float, help='scale for resize')
    args_parser.add_argument('-w', '--width', nargs='?', type = float , help='width for resize')
    args_parser.add_argument('-he', '--height', nargs='?', type = float, help='height for resize')

    args = args_parser.parse_args()
    print(args)
    return args


if __name__ == '__main__':
    args = read_args()
    print(args)

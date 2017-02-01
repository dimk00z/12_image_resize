import argparse
import sys
from PIL import Image
from resizeimage import resizeimage
import os


def resize_image(image, file_name, width, height, scale):
    if scale:
        result_width = image.size[0] * scale
        result_height = image.size[1] * scale
        warning = False
    else:
        result_width = width if width else image.size[0]
        result_height = height if height else image.size[1]
        warning = True
    return {'resized_image': resizeimage.resize_cover(image,
                                                      [result_width,
                                                       result_height],
                                                      validate=False),
            'output_file_name': "{}__{}x{}{}".format(file_name[0],
                                                     str(int(result_width)),
                                                     str(int(result_height)),
                                                     file_name[1]),
            'warning': warning}


def save_resized_image(image, output_file_name):
    image.save(output_file_name, image.format)


def read_args():
    args_parser = argparse.ArgumentParser(prog="Image resizer")
    args_parser.add_argument("image_file_name",
                             type=argparse.FileType('r'), nargs=1,
                             help="Image for resize", default=sys.stdin)
    args_parser.add_argument(
        '-o', '--output', help='output path for new file')
    args_parser.add_argument('-s', '--scale', nargs='?',
                             type=float, help='scale for resize')
    args_parser.add_argument('-w', '--width', nargs='?',
                             type=float, help='width for resize')
    args_parser.add_argument('-he', '--height', nargs='?',
                             type=float, help='height for resize')
    args = args_parser.parse_args()
    if (args.height or args.width) and args.scale:
        return None
    return args


if __name__ == '__main__':
    args = read_args()
    if not args:
        print('Scaling and exact sizes can not be used together.')
        exit()
    image_for_resize = Image.open(args.image_file_name[0].name)
    image_file_name = os.path.splitext(args.image_file_name[0].name)
    resized_image_dict = resize_image(image_for_resize,
                                      image_file_name,
                                      args.width,
                                      args.height,
                                      args.scale)
    if args.output:
        resized_image_dict['output_file_name'] = args.output
    save_resized_image(resized_image_dict['resized_image'], resized_image_dict[
                       'output_file_name'])
    if resized_image_dict['warning']:
        print('The proportions of the images have not been saved.')

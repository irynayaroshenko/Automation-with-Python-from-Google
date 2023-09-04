from concurrent import futures  # added
import argparse
import logging
import os
import sys

import PIL
import PIL.Image

from tqdm import tqdm


def process_options():
    kwargs = {
        'format': '[%(levelname)s] %(message)s',
    }
    parser1 = argparse.ArgumentParser(
        description='Thumbnail generator',
        fromfile_prefix_chars='@'
    )
    parser1.add_argument('--debug', action='store_true')
    parser1.add_argument('-v', '--verbose', action='store_true')
    parser1.add_argument('-q', '--quiet', action='store_true')

    options = parser1.parse_args()

    if options.debug:
        kwargs['level'] = logging.DEBUG
    elif options.verbose:
        kwargs['level'] = logging.INFO
    elif options.quiet:
        kwargs['level'] = logging.ERROR
    else:
        kwargs['level'] = logging.WARN

    logging.basicConfig(**kwargs)

    return options


def process_file(root, basename):
    filename = f'{root}/{basename}'
    image = PIL.Image.open(filename)

    size = (128, 128)
    image.thumbnail(size)

    new_name = f'thumbnails/{basename}'
    image.save(new_name, "JPEG")
    return new_name


def progress_bar(files):
    return tqdm(files, desc='Processing', total=len(files), dynamic_ncols=True)


def main():

    process_options()

    # Create the thumbnail directory
    if not os.path.exists('thumbnails'):
        os.mkdir('thumbnails')

    # executor = futures.ThreadPoolExecutor()  # added on first iteration
    executor = futures.ProcessPoolExecutor()  # added on second iteration
    for root, _, files in os.walk('images'):
        for basename in progress_bar(files):
            if not basename.endswith('.jpg'):
                continue
            # process_file(root, basename)
            executor.submit(process_file, root, basename)  # added
    print('Waiting for all threads to finish.')  # added
    executor.shutdown()  # added
    return 0


if __name__ == "__main__":
    sys.exit(main())


# Created on 11/1/15 by Liam Rahav

import argparse
import os
from imgurpython import ImgurClient
from keys import CLIENT_ID, CLIENT_SECRET
from getopt import getopt


def create_parser():
    p = argparse.ArgumentParser(description="Upload image to imgur")
    p.add_argument('filename', type=str, help="The filename of the image to be uploaded")
    return p


def upload_image():
    print("Starting upload...")
    image = imgur.upload_from_path(
        os.path.dirname(os.path.realpath(args.filename) + "/" + args.filename)
    )
    print("Done!")
    return image


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    imgur = ImgurClient(CLIENT_ID, CLIENT_SECRET)
    image = upload_image()
    print("URL: \033[94m" + image['link'] + "\033[0m")




"""
Script for checking corrupted images

Usage :
    python label_processing.py -d [PATH TO IMAGES FOLDER]

Parameters:
    -d : Path to the folder where the images is stored

RangRang - Machine Learning - 2021
"""

import os, argparse

def is_image(filename, verbose=False):
    """ Checking whether if image is corrupted or not 

    Source : https://stackoverflow.com/a/62544801
    """
    data = open(filename,'rb').read(10)

    # check if file is JPG or JPEG
    if data[:3] == b'\xff\xd8\xff':
        if verbose == True:
             print(filename+" is: JPG/JPEG.")
        return True

    # check if file is PNG
    if data[:8] == b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a':
        if verbose == True:
             print(filename+" is: PNG.")
        return True

    # check if file is GIF
    if data[:6] in [b'\x47\x49\x46\x38\x37\x61', b'\x47\x49\x46\x38\x39\x61']:
        if verbose == True:
             print(filename+" is: GIF.")
        return True

    return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Checking corrupted images.")
    parser.add_argument("-d", 
                        "--image_dir",
                        help="Path to image directory",
                        type=str)
    args = parser.parse_args()

    if args.image_dir:
        # go through all files in desired folder
        for filename in os.listdir(args.image_dir):
            # check if file is actually an image file
            if os.path.splitext(filename)[1] in ['.jpg', '.jpeg', '.png', '.gif']:
                filename = os.path.join(args.image_dir, filename)
                if is_image(filename, verbose=False) == False:
                    # if the file is not valid, remove it
                    print(filename)

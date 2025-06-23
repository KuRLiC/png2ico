#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image

def convert_png_to_ico(png_filename):
    # Open the PNG file
    img = Image.open(png_filename)

    # Standard sizes for ICO files
    # These sizes are commonly used for icons in Windows applications
    sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]

    # Save the image as an ICO file with the specified sizes
    # The ICO format can contain multiple images of different sizes
    ico_filename = png_filename.replace('.png', '.ico')
    img.save(ico_filename, format='ICO', sizes=sizes)

    print(f"File ICO saved as: {ico_filename}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python png2ico.py <image1.png> [<image2.png> ...]")
        exit(1)
    else:
        try:
            for arg in sys.argv[1:]:
                convert_png_to_ico(arg)
        except Exception as e:
            print(f"An error occurred: {e}")
            exit(1)
    exit(0)

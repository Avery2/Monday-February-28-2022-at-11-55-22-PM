import os
from PIL import Image

if __name__ == "__main__":
    im = Image.open("chris.png")
    width, height = im.size
    im = im.resize((int(width/3), int(height/3)))

    # split() method
    # this will split the image in individual bands
    # and return a tuple
    im1 = Image.Image.split(im)

    # showing each band
    # im1[0].show()
    # im1[1].show()
    # im1[2].show()
    for idx, i in enumerate(im1):
        i.save(f"{idx}.png")

    n = 10
    with open("index.md", "x") as f:
        for i in range(n * 3 + 1):
            f.write(f"# \n\n")
            f.write(f"![]({i%3}.png)\n\n")

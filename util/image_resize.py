from PIL import Image
import os,sys
from resizeimage import resizeimage
path = "images/black_eyed_peas/test/"
out="images/black_eyed_peas/testresize/"
# path = "images/brown_gram/test/"
# out="images/brown_gram/testr/"
# path = "images/green_gram/test/"
# out="images/green_gram/testr/"
# path = "images/green_peas/test/"
# out="images/green_peas/testr/"
# path = "images/split_bengal_gram/test/"
# out="images/split_bengal_gram/testr/"


"""
For each category few images are downloaded from google images to prepare test set and saved them in test folder
Then resized these images such that it maintains aspect ratio using image-resize.py and saved those files in test resize sub-folder of each category folder.
"""
def resize_file(in_file, out_file, size):
    # with open(in_file) as fd:
    im=Image.open(in_file)
    rgb_im = im.convert('RGB')
    image = resizeimage.resize_thumbnail(rgb_im, size)
    image.save(out_file)
    image.close()

for f in os.listdir(path):
    resize_file(path+f, out+f+"_small.jpg", (256, 256))
import shutil
import os

"""

Images under test-resize subfolder of each category are copied to common test folder by renaming it as per category it belongs to.
"""

src_dir = "C:/Users/DheerajSingh/Documents/products/images/split_bengal_gram/testresize"
dest_dir = "C:/Users/DheerajSingh/Documents/pulses/test_img/"



for i,f in enumerate(os.listdir(src_dir)):
    shutil.move(os.path.join(src_dir,f),os.path.join(dest_dir,"test_SBG_"+str(i)+".jpg"))
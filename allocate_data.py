import os
import shutil
import random

dir_path = '/Users/sunbowen/Desktop/testImages'
destination = '/Users/sunbowen/Desktop/newImgTest'

# Rename files from .jpeg to .jpg
def rename():
    files = os.listdir(dir_path)

    for file in files:
        pre, ext = os.path.splitext(file)
        os.rename(dir_path + '/' + file, dir_path + '/' + pre + '.jpg')


# allocate data to train and test
def allocate_data():
    files = random.sample(os.listdir(dir_path), 22)

    for file in files:
        srcpath = os.path.join(dir_path, file)
        print(srcpath)
        shutil.move(srcpath, destination, copy_function=shutil.copytree)


if __name__ == "__main__":
    # allocate_data()
    rename()

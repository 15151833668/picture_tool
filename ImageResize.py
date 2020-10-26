# -*- coding: UTF-8 -*-
import os
import sys
import cv2 as cv
from PIL import Image


# 批量图片比例缩放
def image_resize_percent_bitch(file_open_folder, file_save_folder, fx, fy):
    cur_path = os.getcwd()
    if not os.path.exists(cur_path + '/' + file_save_folder):
        os.mkdir(cur_path + '/' + file_save_folder)

    files = os.listdir(cur_path + '/' + file_open_folder)
    for fileName in files:
        if fileName.endswith(".JPEG") \
                or fileName.endswith(".png") \
                or fileName.endswith(".jpeg") \
                or fileName.endswith(".jpg"):
            image = cv.imread(file_open_folder + "/" + fileName)
            new_image = cv.resize(image, None, fx=float(fx), fy=float(fy))
            cv.imwrite(cur_path + '/' + file_save_folder + "/" + fileName, new_image)


# 单张图片具体像素缩放
def image_resize_pixel(input_file, output_file, x, y):
    Image.open(input_file).resize((x, y), Image.ANTIALIAS).save(output_file)


def image_resize_pixel_bitch(file_open_folder, file_save_folder, wide, height):
    cur_path = os.getcwd()
    if not os.path.exists(cur_path + '/' + file_save_folder):
        os.mkdir(cur_path + '/' + file_save_folder)

    files = os.listdir(cur_path + '/' + file_open_folder)
    count = 0
    for file_name in files:
        count += 1
        print("已完成:", count, '/', len(files))
        if file_name.endswith(".JPEG") \
                or file_name.endswith(".png") \
                or file_name.endswith(".jpeg") \
                or file_name.endswith(".jpg"):
            image_resize_pixel(cur_path + '/' + file_open_folder + '/' + file_name,
                               cur_path + '/' + file_save_folder + '/' + file_name,
                               int(wide), int(height))


if __name__ == '__main__':
    # image_resize_percent('compress', 'resize', 0.5, 0.5)

    # image_resize_pixel("/Users/c/PycharmProjects/pictureTool/compress/p2.jpg",
    #
    #                    "/Users/c/PycharmProjects/pictureTool/compress/p2__resize.jpg", 906, 540)
    if (int(sys.argv[1])) == 1:
        image_resize_pixel_bitch('prepare', 'resize', sys.argv[2], sys.argv[3])

    else:
        image_resize_percent_bitch('prepare', 'resize', sys.argv[2], sys.argv[3])
    # image_resize_pixel_bitch('prepare', 'resize', 960, 540)

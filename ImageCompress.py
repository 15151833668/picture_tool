# -*- coding: UTF-8 -*-
import os
import sys
import shutil
import cv2 as cv
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
from sklearn.utils import shuffle


def compression(img, n_colors):
    # transform image into 2D numpy array
    print(img.shape)
    w, h, d = tuple(img.shape)
    img_arr = np.reshape(img, (w * h, 3))
    # fitting sample to kmeans with n_colors being the number of colors
    img_arr_sample = shuffle(img_arr, random_state=0)[:1000]
    kmeans = KMeans(n_clusters=n_colors).fit(img_arr_sample)
    # get labels for predictor
    labels = kmeans.predict(img_arr)
    return kmeans, labels, w, h


def reshape_image(img, labels, w, h):
    # restructure image for plt.imshow()
    output = np.zeros((w, h, 3))
    index = 0
    for i in range(w):
        for j in range(h):
            output[i][j] = img[labels[index]]
            index += 1
    return output


def K_means(original_image, n_colors):
    # perform k-means using n_colors centroids
    kmeans, labels, w, h = compression(original_image, n_colors)
    # restructure image for output
    new_img = reshape_image(kmeans.cluster_centers_, labels, w, h)
    # returns new image in form of numpy array
    return new_img


def png2_image_compress(src_image_path, save_dir, image_name):
    original_image = np.array(Image.open(src_image_path))
    levels = {1: 200, 2: 100, 3: 50, 4: 25, 5: 5}
    l = int(input("What level of compression would you like? (1-5): "))

    n_im = K_means(original_image, levels[l])
    n_im = n_im.astype('uint8')
    img = Image.fromarray(n_im, 'RGB')
    if not str(save_dir).endswith('/'):
        save_dir += '/'
    save_name = save_dir + str(image_name).split('.')[0] + "_compress.png"
    # img.show("img", img)
    print(save_name)
    img.save(save_name)


#  压缩jpg jpeg格式图片
def jpg_image_compress(folder_prepare, folder_compress, file_name, quality):
    cur_path = os.getcwd()
    save_path = cur_path + '/' + folder_compress
    # if not os.path.exists(save_path):
    #     os.mkdir(save_path)
    src_image_path = cur_path + '/' + folder_prepare + '/' + file_name

    img = cv.imread(src_image_path, 1)
    cv.imwrite(save_path + '/' + file_name, img, [cv.IMWRITE_JPEG_QUALITY, int(quality)])  # quality 15,


# 压缩png格式图片
def png_image_compress(folder_prepare, folder_compress, file_name, level):
    cur_path = os.getcwd()
    src_image_path = cur_path + '/' + folder_prepare + '/' + file_name
    print('src_image_path: ', src_image_path)
    original_image = np.array(Image.open(src_image_path))
    levels = {1: 200, 2: 100, 3: 50, 4: 25, 5: 5}
    n_im = K_means(original_image, levels[int(level)])
    n_im = n_im.astype('uint8')
    img = Image.fromarray(n_im, 'RGB')
    name = cur_path + "/" + folder_compress + '/' + file_name
    # img.show("img", img)
    print(name)
    img.save(name)


def compress_image(folder_prepare, folder_compress, level, quality):
    cur_path = os.getcwd()
    src_path = cur_path + '/' + folder_prepare
    save_path = cur_path + '/' + folder_compress
    if os.path.exists(save_path):
        shutil.rmtree(save_path)
    os.mkdir(save_path)
    files = os.listdir(src_path)
    count = 0
    for file_name in files:
        count += 1
        print("已完成:", count, '/', len(files))

        if file_name.endswith(".png"):
            png_image_compress(folder_prepare=folder_prepare,
                               folder_compress=folder_compress,
                               file_name=file_name,
                               level=level)

        elif file_name.endswith(".jpeg") or file_name.endswith(".jpg"):
            jpg_image_compress(folder_prepare=folder_prepare,
                               folder_compress=folder_compress,
                               file_name=file_name, quality=quality)
        else:
            continue


def replace_dir(src_dir, dst_dir):
    if os.path.exists(src_dir):
        shutil.rmtree(dst_dir)
        os.rename(src_dir, dst_dir)


if __name__ == '__main__':
    folder_prepare = 'prepare'

    folder_compress = 'compress'
    dst_dir = os.getcwd() + '/' + folder_prepare
    src_dir = os.getcwd() + '/' + folder_compress
    print('正在进行图片批量压缩')
    compress_image(folder_prepare, folder_compress, sys.argv[1], sys.argv[2])
    print("图片存放路径： ", dst_dir)
    replace_dir(src_dir, dst_dir)
    # folder_prepare = 'prepare'
    # folder_compress = 'compress'
    # compress_image(folder_prepare, folder_compress, 4, 15)

# -*- coding: UTF-8 -*-

import os
import cv2 as cv
import numpy as np
from PIL import Image, ImageFont, ImageDraw


def image_watermark_by_image(image_path, mark_path, post):
    im = Image.open(image_path)
    mark = Image.open(mark_path)
    layer = Image.new('RGBA', im.size, (0, 0, 0, 0))
    layer.paste(mark, post)
    out = Image.composite(layer, im, layer)
    out.show()


#  图片水印
def image_watermark_by_image(image_path, mark_path, save_dir, file_name):
    img = cv.imread(image_path)
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    h, w = img.shape[0], img.shape[1]
    mark = cv.imread(mark_path)
    mark_h, mark_w = mark.shape[0], mark.shape[1]
    print("原图高：" + str(h) + "原图宽" + str(w) + "水印高：" + str(mark_h) + "水印宽" + str(mark_w))
    # 根据小图像的大小，在大图像上创建感兴趣区域roi（放置位置任意取）
    rows, cols = mark.shape[:2]  # 获取水印的高度、宽度
    # 水印应该在图片的右下角
    roi = img[h - mark_h:h, w - mark_w:w]  #
    roi.shape  # 获取原图roi
    print(roi.shape[:2])  # 打印roi大小
    dst = cv.addWeighted(mark, 1, roi, 1, 0)  # 图像融合
    add_img = img.copy()  # 对原图像进行拷贝
    add_img[h - mark_h:h, w - mark_w:w] = dst  # 将融合后的区域放进原图
    # 保存添加水印后的图片
    cv.imwrite(save_dir + '/' + file_name, add_img)


#  文字水印
def image_watermark_by_words(image_path, file_name, file_save_dir, pos, keyword):
    img1 = cv.imread(image_path, cv.IMREAD_COLOR)
    pil_image = Image.fromarray(cv.cvtColor(img1, cv.COLOR_BGR2RGB))
    font = ImageFont.truetype('Arial Unicode.ttf', 100)
    color = (0, 0, 255)
    draw = ImageDraw.Draw(pil_image)
    draw.text(pos, keyword, font=font, fill=color)
    cv_img = cv.cvtColor(np.asarray(pil_image), cv.COLOR_RGB2BGR)
    cv.imshow('image', cv_img)
    # cv.waitKey(0)
    cv.imwrite(file_save_dir + '/_water' + file_name, cv_img)


if __name__ == '__main__':
    print()
    # 文字水印
    image_watermark_by_words('/Users/c/PycharmProjects/pictureTool/prepare/p1.jpeg',
                             "p1.jpeg",
                             "/Users/c/PycharmProjects/pictureTool/prepare",
                             (480, 480),
                             "小懵科技\n"
                             "123456789")

    image_watermark_by_image("/Users/c/PycharmProjects/pictureTool/prepare/p3.png",
                             "/Users/c/PycharmProjects/pictureTool/resize/p2.jpg",
                             "/Users/c/PycharmProjects/pictureTool/watermark",
                             "p3.png")

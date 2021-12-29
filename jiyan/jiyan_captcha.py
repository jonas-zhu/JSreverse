# -*- coding: utf-8 -*-
import sys
sys.path.append("../")
import io
from pathlib import Path
from PIL import Image


def restore_image(img, im_show=False, save_path=None):
    if isinstance(img, (str, Path)):
        base_pic = Image.open(img)
    elif isinstance(img, bytes):
        base_pic = Image.open(io.BytesIO(img))
    else:
        raise ValueError(f'输入图片类型错误, 必须是<type str>/<type Path>/<type bytes>: {type(img)}')

    Ut = [39, 38, 48, 49, 41, 40, 46, 47, 35, 34, 50, 51, 33, 32, 28, 29, 27, 26, 36, 37, 31, 30, 44, 45, 43, 42, 12, 13, 23, 22, 14, 15, 21, 20, 8, 9, 25, 24, 6, 7, 3, 2, 0, 1, 11, 10, 4, 5, 19, 18, 16, 17]
    w_sep, h_sep = 10, 80
    pic_width = 260
    pic_height = r = 160
    a = int(r / 2)
    # 还原后的图片
    new_img = Image.new("RGB", (pic_width, pic_height))

    for index in range(0, 52):
        x = Ut[index] % 26 * 12 + 1
        y = a if 25 < Ut[index] else 0
        # print((x, y, x+w_sep, y+h_sep))
        # 从背景图中裁剪出对应位置的小块
        img_cut = base_pic.crop((x, y, x+w_sep, y+h_sep))
        # 将小块拼接到新图中
        new_img.paste(img_cut, (int(index % 26 * 10), a if 25 < index else 0))
    if im_show:
        new_img.show()
    if save_path is not None:
        save_path = Path(save_path).resolve().__str__()
        new_img.save(save_path)
    return save_path


if __name__ == '__main__':
    restore_image("bg.webp", im_show=True, save_path='bg.png')



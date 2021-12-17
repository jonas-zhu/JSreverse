import cv2 as cv
import numpy as np


class SlideCrack(object):
    def __init__(self, gap, bg, out, out_flag=True):
        """
        init code
        :param gap: 缺口(滑块)图片
        :param bg: 背景图片
        :param out: 输出图片
        """
        self.gap = gap
        self.bg = bg
        self.out = out
        self.out_flag = out_flag

    @staticmethod
    def clear_white(img):
        # 清除图片的空白区域，这里主要清除滑块的空白
        # img = cv.imread(img)
        rows, cols, channel = img.shape
        min_x = 255
        min_y = 255
        max_x = 0
        max_y = 0
        for x in range(1, rows):
            for y in range(1, cols):
                t = set(img[x, y])
                if len(t) >= 2:
                    if x <= min_x:
                        min_x = x
                    elif x >= max_x:
                        max_x = x

                    if y <= min_y:
                        min_y = y
                    elif y >= max_y:
                        max_y = y
        img1 = img[min_x:max_x, min_y: max_y]
        return img1

    def template_match(self, tpl, target):
        th, tw = tpl.shape[:2]
        result = cv.matchTemplate(target, tpl, cv.TM_CCOEFF_NORMED)
        # 寻找矩阵(一维数组当作向量,用Mat定义) 中最小值和最大值的位置
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        tl = max_loc
        if self.out_flag:
            # 绘制矩形边框，将匹配区域标注出来
            # target：目标图像
            # tl：矩形定点
            # br：矩形的宽高
            # (0,0,255)：矩形边框颜色
            # 1：矩形边框大小
            br = (tl[0] + tw, tl[1] + th)
            cv.rectangle(target, tl, br, (0, 0, 255), 2)
            cv.imwrite(self.out, target)
        return tl[0]

    @staticmethod
    def image_edge_detection(img):
        edges = cv.Canny(img, 100, 200)
        return edges

    def discern(self, scale_ratio):
        img1 = cv.imread(self.gap)
        img1 = cv.resize(img1, (int(img1.shape[1] * scale_ratio), int(img1.shape[0] * scale_ratio)), interpolation=cv.INTER_AREA)
        img1 = self.clear_white(img1)
        img1 = cv.cvtColor(img1, cv.COLOR_RGB2GRAY)
        slide = self.image_edge_detection(img1)

        back = cv.imread(self.bg, 0)
        back = cv.resize(back, (int(back.shape[1] * scale_ratio), int(back.shape[0] * scale_ratio)), interpolation=cv.INTER_AREA)
        back = self.image_edge_detection(back)

        slide_pic = cv.cvtColor(slide, cv.COLOR_GRAY2RGB)
        back_pic = cv.cvtColor(back, cv.COLOR_GRAY2RGB)
        x = self.template_match(slide_pic, back_pic)
        # 输出横坐标, 即 滑块在图片上的位置
        print(x)
        return x


def discern_gap(gapImage: bytes, sliderImage: bytes, show=False):
    """
    :param gapImage: 背景图片
    :param sliderImage: 缺口(滑块)图片
    :param show: 展示图片
    """
    def edge_detection(rawimg):
        def tracebar(x):
            threshold1 = cv.getTrackbarPos('threshold1', 'Test')
            threshold2 = cv.getTrackbarPos('threshold2', 'Test')
            edged_img = cv.Canny(img_Gaussian, threshold1, threshold2)
            cv.imshow("edged_img", edged_img)

        image = np.asarray(bytearray(rawimg), dtype="uint8")
        img = cv.imdecode(image, cv.IMREAD_COLOR)
        grep_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        # 高斯滤波 高斯滤波是通过对输入数组的每个点与输入的高斯滤波模板执行卷积计算然后将这些结果一块组成了滤波后的输出数组，
        # 通俗的讲就是高斯滤波是对整幅图像进行加权平均的过程，每一个像素点的值都由其本身和邻域内的其他像素值经过加权平均后得到。
        # 高斯滤波的具体操作是：用一个模板（或称卷积、掩模）扫描图像中的每一个像素，用模板确定的邻域内像素的加权平均灰度值去替代模板中心像素点的值。
        img_Gaussian = cv.GaussianBlur(grep_img, (5, 5), 0)
        # 用于对图像的边缘检测
        edged_img = cv.Canny(img_Gaussian, 25, 45)
        if show:
            cv.namedWindow("Test")
            # cv.imshow('raw_img', img)
            # cv.imshow('grep_img', grep_img)
            cv.imshow('img_Gaussian', img_Gaussian)
            cv.createTrackbar("threshold1", "Test", 0, 255, tracebar)
            cv.createTrackbar("threshold2", "Test", 0, 255, tracebar)
            # cv.imshow('edged_img', edged_img)
            cv.waitKey()
            cv.destroyAllWindows()
        return edged_img

    def similarity_calculation(background, slider):
        result = cv.matchTemplate(background, slider, cv.TM_CCOEFF_NORMED)
        # 获取一个/组int类型的索引值在一个多维数组中的位置。
        # x, y = np.unravel_index(result.argmax(), result.shape)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        return max_loc

    """计算滑动距离方法"""
    gap = edge_detection(gapImage)
    slider = edge_detection(sliderImage)
    x, y = similarity_calculation(gap, slider)
    # print('需要滑动距离', x, y)
    # todo 返回的距离
    return x


if __name__ == "__main__":
    '''
    # 滑块图片  447
    tigerPath = "fg.png"
    # 背景图片
    dragonPath = "bg.png"

    # 处理结果图片,用红线标注
    processedPath = "result.png"
    sc = SlideCrack(tigerPath, dragonPath, processedPath)
    slide_length = sc.discern()
    '''
    ''' 446
    gapImage = open('bg.png', mode='rb').read()
    sliderImage = open('fg.png', mode='rb').read()
    slide_length = discern_gap(gapImage, sliderImage, show=True)
    print(slide_length)
    '''


